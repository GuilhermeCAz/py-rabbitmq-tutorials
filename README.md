# RabbitMQ Tutorials with Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![RabbitMQ Logo](https://img.shields.io/badge/RabbitMQ-%23636363?logo=rabbitmq)](https://www.rabbitmq.com/)
[![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FGuilhermeCAz%2Fshurl_django%2Fmain%2Fpyproject.toml&logo=python&label=Python)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

This project is a hands-on exploration of RabbitMQ using Python. It follows the tutorials provided by RabbitMQ's official documentation to demonstrate basic messaging patterns and concepts.

## Project Structure

The project is organized into two main applications under the `src` directory:

- [**queues**](src/queues): Contains implementations for RabbitMQ messaging using queues.
- [**streams**](src/streams): Contains implementations for RabbitMQ messaging using streams.

Each tutorial or concept is structured in its own directory, following a modular approach for easy understanding and experimentation.

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

- Python installed on your machine.
- RabbitMQ server running locally or accessible via network.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/GuilhermeCAz/py-rabbitmq-tutorials
   cd py-rabbitmq-tutorials
   ```

2. Install dependencies:

   ```bash
   uv install
   ```

### Running the Tutorials

Each tutorial is in a separate folder under the `src/queues` or `src/streams` directory. To run a tutorial, simply follow the instructions in the `INSTRUCTIONS.md` file of the tutorial.

## Resources

[RabbitMQ Tutorials](https://www.rabbitmq.com/tutorials)

## Contributing

Contributions are welcome! If you find any issues or improvements, please submit an issue or a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
