"""Same-padded convolution with Kaiming-normal initialization.
"""
import torch as th

class _Conv2d(th.nn.Conv2d):
    """Same-padded convolution with Kaiming-normal initialization.
    """
    def __init__(self, in_chans, out_chans, kernel_size, bias=True):
        """Initialize a same-padded convolutional layer.

        Args:
            in_chans (int):
                Number of input channels.
            out_chans (int):
                Number of output channels.
            kernel_size (int):
                Size of the convolutional kernel.
            bias (bool):
                Whether to include an additive bias.
        """
        super().__init__(
            in_chans, out_chans,
            kernel_size=kernel_size,
            padding='same',
            bias=bias,
        )

    def reset_parameters(self):
        """Initialize weights with Kaiming-normal values and biases with zeros.
        """
        th.nn.init.kaiming_normal_(self.weight, nonlinearity='linear')
        if getattr(self, 'bias', None) is not None:
            th.nn.init.zeros_(self.bias)
