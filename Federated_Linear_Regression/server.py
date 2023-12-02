import flwr as fl
import data
import utils
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error as mean
from typing import Dict


def fit_round(server_round: int) -> Dict:
    """Send round number to client."""
    return {"server_round": server_round}


def get_evaluate_fn(model: LinearRegression):
    """Return an evaluation function for server-side evaluation."""

    # Load test data
    test_data = data.load_data("test")
    x_test = test_data.drop("calories_to_maintain_weight", axis=1)
    y_test = test_data["calories_to_maintain_weight"]

    # The `evaluate` function will be called after every round
    def evaluate(server_round, parameters: fl.common.NDArrays, config):
        # Update model with the latest parameters
        utils.set_model_params(model, parameters)
        loss = mean(y_test, model.predict(x_test))
        return loss, {}

    return evaluate


# Start Flower server for five rounds of federated learning

if __name__ == "__main__":
    model = LinearRegression()
    utils.set_initial_params(model)

    strategy = fl.server.strategy.FedAvg(
        min_available_clients=2,
        evaluate_fn=get_evaluate_fn(model),
        on_fit_config_fn=fit_round,
    )
    fl.server.start_server(
        server_address="localhost:8080",
        strategy=strategy,
        config=fl.server.ServerConfig(num_rounds=5),
    )
