"""Bilinear upsampling to a specified spatial size.
"""
import torch as th

class _Upsample(th.nn.Module):
    """Bilinear upsampling layer.

    Input:
        x (torch.Tensor):
            Input tensor with shape ``(N, C, H, W)``.
        size (tuple[int, int]):
            Target spatial dimensions ``(H_out, W_out)``.

    Output:
        Upsampled tensor with shape ``(N, C, H_out, W_out)``.
    """
    def forward(self, x, size):
        """Upsample the input to the target size.
        """
        return th.nn.functional.interpolate(
            x, size=size, mode='bilinear', align_corners=False)
