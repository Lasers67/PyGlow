import numpy as np
import torch
from torch import nn
from tqdm import tqdm


class Dynamics:
    """
    Class for evaluating all the dynamics related coordinates

    """

    def __init__(self, dynamics_segment):
        self.dynamics_segment = dynamics_segment

    def evaluate(self, evaluator_obj):
        """
        # ** NOTE - This can be done in parallel !
        epoch_output = []
        print("\n")
        num_epochs = len(self.dynamics_collector)
        print("Evaluating " + str(evaluator_obj.__class__) + "for dynamics")
        for idx, epoch_collector in enumerate(self.dynamics_collector):
            print(
                "Evaluating epoch " + str(idx + 1) + "/" + str(num_epochs) + " dynamics"
            )
            batch_output = []
            pbar = tqdm(total=len(epoch_collector))
            for batch_collector in epoch_collector:
                dynamics_segment = batch_collector
                output_segment = evaluator_obj.eval_dynamics_segment(dynamics_segment)
                batch_output.append(output_segment)
                pbar.update(1)
            pbar.close()
            epoch_output.append(batch_output)
        """
        evaluated_segment = evaluator_obj.eval_dynamics_segment(self.dynamics_segment)
        return evaluated_segment

    def plot_dynamics(self, evaluated_dynamics):
        x_axis = []
        y_axis = []
        for epoch_collector in evaluated_dynamics:
            for batch_collector in epoch_collector:
                for segment in batch_collector:
                    x_axis.append(segment[0])
                    y_axis.append(segment[1])


def get(identifier):
    return Dynamics(identifier)
