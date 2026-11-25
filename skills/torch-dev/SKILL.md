---
name: torch-dev
description: Apply the user's conventions when writing or editing PyTorch code.
  Consult this skill when those conventions are unfamiliar or no longer in
  context. Includes reusable layer implementations.
---

# PyTorch Development

Follow the project's conventions unless the user requests otherwise. Use these
preferences where the project leaves room for them. Carry the guidance already
in context into follow-up edits and open the relevant asset when needed.

## Imports and names

Use `import torch as th` and qualified names such as `th.nn.Module` and
`th.nn.functional.relu`. Use descriptive names when unpacking shapes, such as
`batch_size, num_chans, height, width = x.shape`.

- Use `in_chans` and `out_chans` for image channels, or `num_chans` when one
  count suffices. For generic features, use `in_feat`, `out_feat`, and
  `num_feat`.
- Use `_dim` for representation dimensions such as `attn_dim`. Use count names
  such as `num_hidden` and `attn_heads` where they describe the argument better.

## Tensor operations

Use `moveaxis` when moving a single axis. For example, on a batched
channel-first tensor, `x.moveaxis(1, -1)` moves channels last without
enumerating the spatial axes. `x.moveaxis(-1, 1)` moves them back. Use
`dim=-1` for operations on the trailing feature axis, as in
`th.cat((x, w), dim=-1)`. Prefer `_like` constructors such as
`th.zeros_like(x)` when the desired shape, dtype, and device match.

Let extra ranks work naturally where the operation allows it. Document the
shapes the layer is designed to support and treat other shapes that happen to
work as incidental. Use simple assertions for internal shape assumptions when
they clarify the code or help verify the computation.

Use `x` for a generic input to `forward` and rebind it as the main path
advances when the previous value has no further use.

```python
def forward(self, x):
    """Project and normalize the input.
    """
    x = self.visible(self.hidden(x))
    return self.norm(x)
```

Use `r` for the residual branch and keep `x` for the addition.

```python
def forward(self, x):
    """Add the normalized residual to the input.
    """
    r = self.visible(self.hidden(x))
    r = self.norm(r)
    return x + r
```

## Module design

Use `th.nn.Sequential` for straight pipelines and `th.nn.ModuleList` when
`forward` does work between layers. Prefer a named module over a factory or
`partial` when initialization is complex or worth reusing, or when the block
needs its own `forward`. Subclass a container when it fits the module's role.
Use `layer_in` and `layer_out` when tracking widths across layers improves
clarity.

Generally prefer activation modules such as `th.nn.ReLU()` so the activation
is visible when inspecting the model. Use the functional form when it fits
the surrounding computation better.

Use `register_buffer` for tensors computed once or infrequently that should
follow the module across devices, or for tensor state that needs to be saved
and restored through `state_dict`. Compute values that change with each call
in `forward`.

## Bundled layers

Copy a bundled implementation as written when it fits and adapt it when the
project requires it.

- [`_Linear`](assets/linear.py) uses Kaiming normal initialization with linear
  gain and zero bias.
- [`_Conv2d`](assets/conv2d.py) uses same padding and the same initialization.
- [`_GroupNorm`](assets/group_norm.py) uses a tapered default group count.
