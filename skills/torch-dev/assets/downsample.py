"""Binomial-filtered spatial downsampling by a factor of two.
"""
import torch as th

class _Downsample(th.nn.Module):
    """Downsampling with a separable three-tap binomial anti-aliasing filter.

    Input:
        x (torch.Tensor):
            Input tensor with shape ``(N, C, H, W)``.

    Output:
        Downsampled version of the input tensor with shape
        ``(N, C, (H + 1) // 2, (W + 1) // 2)``.
    """
    def __init__(self):
        """Initialize the binomial filter.
        """
        super().__init__()

        # Normalize the separable kernel for unit DC gain and store it as a
        # non-persistent buffer.
        kernel = th.as_tensor([1., 2., 1.])
        kernel /= kernel.sum()
        self.register_buffer('kernel', kernel, persistent=False)

    def forward(self, x):
        """Filter and downsample the input.
        """
        batch_size, num_chans, height, width = x.shape

        # Place the channels on the batch dim since we apply the same
        # filter to all batches and all channels.
        x = x.reshape(-1, 1, height, width)

        # We use replication padding
        x = th.nn.functional.pad(x, (1,)*4, mode='replicate')

        # Apply the spatially separable filter along both axes
        x = th.conv2d(x, self.kernel[None, None, :, None], stride=(2, 1))
        x = th.conv2d(x, self.kernel[None, None, None, :], stride=(1, 2))
        _, _, new_height, new_width = x.shape

        # Place channels back on the correct dim
        return x.contiguous().view(batch_size, num_chans, new_height, new_width)
