"""Group normalization with tapered groups for small channel counts.
"""
import torch as th

class _GroupNorm(th.nn.GroupNorm):
    """Group normalization with tapered groups for small channel counts.

    Input:
        input (torch.Tensor):
            Tensor with shape ``(N, num_chans, *)``, where ``*`` denotes zero
            or more spatial dimensions.

    Output:
        Normalized tensor with the same shape as the input.
    """
    def __init__(self, num_chans, num_groups=None, **kwargs):
        """Initialize group normalization with a tapered default group count.

        Args:
            num_chans (int):
                Number of channels.
            num_groups (None | int):
                Number of groups. Derived from ``num_chans`` when omitted.
            **kwargs (dict):
                Additional arguments passed to ``th.nn.GroupNorm``.
        """
        if num_groups is None:
            num_groups = self._init_num_groups(num_chans)

        super().__init__(num_groups=num_groups, num_channels=num_chans, **kwargs)

    @staticmethod
    def _init_num_groups(num_chans):
        """Choose a tapered default group count for the given channels.
        """
        if num_chans < 8:
            return 1
        if num_chans < 16:
            return 2
        if num_chans < 32:
            return 4

        return 8
