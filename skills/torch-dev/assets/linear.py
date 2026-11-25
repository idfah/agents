"""Linear layer with Kaiming-normal initialization.
"""
import torch as th

class _Linear(th.nn.Linear):
    """Linear layer with Kaiming-normal weight initialization.

    Input:
        input (torch.Tensor):
            Tensor with shape ``(*, in_features)``, where ``*`` denotes zero
            or more leading dimensions.

    Output:
        Tensor with shape ``(*, out_features)`` and the same leading
        dimensions as the input.
    """
    def reset_parameters(self):
        """Initialize weights with Kaiming-normal values and biases with zeros.
        """
        th.nn.init.kaiming_normal_(self.weight, nonlinearity='linear')
        if self.bias is not None:
            th.nn.init.zeros_(self.bias)
