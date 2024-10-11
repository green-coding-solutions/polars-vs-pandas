## Polars vs. Pands

This is a test repository to evaluate the CPU time, CPU energy and Memory Energy for a typical
pandas operation compared to a polars operation as we use it in the [Green Metrics Tool](https://www.green-coding.io/projects/green-metrics-tool/).

Although our data-wrangling is more on the small side (Files typically are less than 100 MB) we are an open source
software and the operation is done on many machines for many users.

Polars seems like an interesting candidate as we actually do column based operations more than row based operations.

This repo tries to evaluate if in the end polars is better for our use case or if it just saves time but maybe consumes
more energy to achieve the goal (through more memory use, more costly operations or simply parallization).

## Results

https://metrics.green-coding.io/repositories.html?uri=https://github.com/green-coding-solutions/polars-vs-pandas