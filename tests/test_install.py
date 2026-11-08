"""Tests for the personal agent configuration installer.
"""

import importlib.machinery
import importlib.util
import pathlib
import tomllib

import click.testing
import pytest
import yaml

# Load the extensionless executable for direct Click invocation
loader = importlib.machinery.SourceFileLoader(
    'installer', str(pathlib.Path(__file__).parents[1] / 'scripts/install'),
)
spec = importlib.util.spec_from_loader(loader.name, loader)
install = importlib.util.module_from_spec(spec)
loader.exec_module(install)

def run_command(monkeypatch, tmp_path, *arguments):
    """Invoke the installer against a temporary home directory.

    Args:
        monkeypatch (pytest.MonkeyPatch):
            Pytest monkeypatch fixture.
        tmp_path (pathlib.Path):
            Pytest temporary directory fixture.
        arguments (tuple[str, ...]):
            Command-line arguments.

    Returns (click.testing.Result):
        Click command result.
    """
    monkeypatch.setattr(pathlib.Path, 'home', lambda: tmp_path)
    runner = click.testing.CliRunner()
    result = runner.invoke(install.command, arguments)
    assert result.exit_code == 0, result.output
    return result

def test_codex_install_replaces_managed_files(monkeypatch, tmp_path):
    """Codex installation should replace managed files and preserve local files.
    """
    run_command(monkeypatch, tmp_path, 'codex')
    codex_home = tmp_path / '.codex'
    installed_agent = codex_home / 'agents/algorithms_expert.toml'
    local_agent = codex_home / 'agents/local_agent.toml'
    with installed_agent.open('rb') as file:
        agent_config = tomllib.load(file)
    assert agent_config['sandbox_mode'] == 'read-only'
    assert agent_config['model_reasoning_effort'] == 'high'
    assert (codex_home / 'skills/context-warmup/agents/openai.yaml').is_file()
    installed_agent.write_text('local changes\n')
    local_agent.write_text('local agent\n')
    (codex_home / 'AGENTS.md').write_text('local instructions\n')
    run_command(monkeypatch, tmp_path, 'codex')
    assert installed_agent.read_text() != 'local changes\n'
    assert local_agent.read_text() == 'local agent\n'
    assert (codex_home / 'AGENTS.md').read_text() == (
        install.repository_root / 'codex/AGENTS.md'
    ).read_text()

def test_claude_install_renders_native_agents(monkeypatch, tmp_path):
    """Claude installation should omit Codex-specific metadata.
    """
    run_command(monkeypatch, tmp_path, 'claude')
    claude_home = tmp_path / '.claude'
    installed_agent = claude_home / 'agents/algorithms_expert.md'
    text = installed_agent.read_text()
    frontmatter = text[4:].split('\n---\n', maxsplit=1)[0]
    metadata = yaml.safe_load(frontmatter)
    assert metadata['model'] == 'opus'
    assert metadata['tools'] == 'Read, Grep, Glob, Bash, WebSearch, WebFetch'
    assert 'codex' not in metadata
    assert not (claude_home / 'skills/context-warmup/agents/openai.yaml').exists()
    assert (claude_home / 'skills/context-warmup/SKILL.md').is_file()

@pytest.mark.parametrize('target', ('claude', 'codex', 'copilot'))
def test_scaffolding_skill_installs_all_assets(monkeypatch, tmp_path, target):
    """Install templates, including dotfiles, and filter native skill metadata.
    """
    run_command(monkeypatch, tmp_path, target)
    source = install.repository_root / 'skills/new-python-repo'
    destination = tmp_path / f'.{target}/skills/new-python-repo'
    for asset in (source / 'assets').rglob('*'):
        if asset.is_file():
            installed = destination / asset.relative_to(source)
            assert installed.read_bytes() == asset.read_bytes()

    assert (destination / 'assets/.pylintrc').is_file()
    assert (destination / 'assets/.gitignore').is_file()
    assert (destination / 'SKILL.md').read_bytes() == (source / 'SKILL.md').read_bytes()
    assert (destination / 'agents/openai.yaml').exists() == (target == 'codex')

@pytest.mark.parametrize('target', ('claude', 'codex', 'copilot'))
def test_repeat_install_reports_unchanged_files(monkeypatch, tmp_path, target):
    """Repeating an installation should report unchanged files, not replacements.
    """
    run_command(monkeypatch, tmp_path, target)
    suffix = install.targets[target]['subagent_suffix']
    installed_agent = tmp_path / f'.{target}/agents/algorithms_expert{suffix}'
    installed_agent.write_text('local changes\n')
    assert 'replace' in run_command(monkeypatch, tmp_path, target).output
    result = run_command(monkeypatch, tmp_path, target)
    assert 'unchanged' in result.output
    assert 'replace' not in result.output

@pytest.mark.parametrize('target', ('claude', 'codex', 'copilot'))
def test_existing_main_configuration_requires_force(monkeypatch, tmp_path, target):
    """Existing main configuration should change only when forced.
    """
    run_command(monkeypatch, tmp_path, target)
    source, name = install.targets[target]['config']
    settings = tmp_path / f'.{target}' / name
    settings.write_text('local settings\n')
    result = run_command(monkeypatch, tmp_path, target)
    assert settings.read_text() == 'local settings\n'
    assert 'local configuration exists' in result.output
    run_command(monkeypatch, tmp_path, '--force', target)
    assert settings.read_text() == (install.repository_root / source).read_text()

@pytest.mark.parametrize('target', ('claude', 'codex', 'copilot'))
def test_dry_run_makes_no_changes(monkeypatch, tmp_path, target):
    """Dry-run should report planned changes without creating files.
    """
    result = run_command(monkeypatch, tmp_path, '--dry-run', target)
    _, name = install.targets[target]['instructions']
    assert str(tmp_path / f'.{target}' / name) in result.output
    assert not (tmp_path / f'.{target}').exists()

def test_copilot_install_renders_and_refreshes_managed_files(monkeypatch, tmp_path):
    """Copilot should render all roles and refresh only its managed files.
    """
    run_command(monkeypatch, tmp_path, 'copilot')
    copilot_home = tmp_path / '.copilot'
    for source in sorted((install.repository_root / 'subagents').glob('*.md')):
        canonical, body = install.read_subagent(source)
        installed_agent = copilot_home / 'agents' / f'{source.stem}.agent.md'
        frontmatter, installed_body = installed_agent.read_text()[4:].split(
            '\n---\n', maxsplit=1,
        )
        metadata = yaml.safe_load(frontmatter)
        assert metadata['name'] == source.stem
        assert metadata['model'] == canonical['copilot']['model']
        assert metadata['reasoning-effort'] == canonical['copilot']['reasoning_effort']
        assert metadata['tools'] == ['read', 'search', 'execute', 'web']
        assert metadata['strict-tools-list'] is True
        assert metadata['include-custom-instructions'] is True
        assert 'codex' not in metadata
        assert 'claude' not in metadata
        assert installed_body.strip() == body

    instructions = copilot_home / 'copilot-instructions.md'
    skill = copilot_home / 'skills/context-warmup/SKILL.md'
    agent = copilot_home / 'agents/algorithms_expert.agent.md'
    local_agent = copilot_home / 'agents/local.agent.md'
    assert not (copilot_home / 'skills/context-warmup/agents/openai.yaml').exists()
    for managed_file in (instructions, skill, agent):
        managed_file.write_text('local changes\n')
    local_agent.write_text('local agent\n')
    run_command(monkeypatch, tmp_path, 'copilot')
    assert instructions.read_text() == (
        install.repository_root / 'copilot/copilot-instructions.md'
    ).read_text()
    assert skill.read_text() == (
        install.repository_root / 'skills/context-warmup/SKILL.md'
    ).read_text()
    assert agent.read_text() != 'local changes\n'
    assert local_agent.read_text() == 'local agent\n'

def test_copilot_renderer_uses_copilot_model_and_reasoning():
    """Copilot rendering should use its own model and reasoning metadata.
    """
    canonical, body = install.read_subagent(
        install.repository_root / 'subagents/algorithms_expert.md',
    )
    canonical['codex']['model'] = 'gpt-5.6-sol'
    canonical['codex']['reasoning_effort'] = 'high'
    canonical['copilot']['model'] = 'gpt-6.1-sol'
    canonical['copilot']['reasoning_effort'] = 'medium'
    rendered = install.render_copilot_subagent(canonical, body)
    frontmatter = rendered[4:].split('\n---\n', maxsplit=1)[0]
    metadata = yaml.safe_load(frontmatter)
    assert metadata['model'] == 'gpt-6.1-sol'
    assert metadata['reasoning-effort'] == 'medium'

def test_invalid_subagent_reports_a_click_error(monkeypatch, tmp_path):
    """Invalid canonical subagents should produce a clear user-facing error.
    """
    source_root = tmp_path / 'source'
    (source_root / 'codex').mkdir(parents=True)
    (source_root / 'skills/example').mkdir(parents=True)
    (source_root / 'subagents').mkdir()
    (source_root / 'codex/AGENTS.md').write_text('Instructions\n')
    (source_root / 'codex/config.toml').write_text('')
    (source_root / 'skills/example/SKILL.md').write_text('# Example\n')
    (source_root / 'subagents/broken.md').write_text('No frontmatter\n')
    monkeypatch.setattr(install, 'repository_root', source_root)
    monkeypatch.setattr(pathlib.Path, 'home', lambda: tmp_path / 'home')
    result = click.testing.CliRunner().invoke(install.command, ['codex'])
    assert result.exit_code == 1
    assert 'does not start with YAML frontmatter' in result.output
