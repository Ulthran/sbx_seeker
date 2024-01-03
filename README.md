<img src="https://github.com/sunbeam-labs/sunbeam/blob/stable/docs/images/sunbeam_logo.gif" width=120, height=120 align="left" />

# sbx_seeker

<!-- Badges start -->
[![Tests](https://github.com/Ulthran/sbx_seeker/actions/workflows/tests.yml/badge.svg)](https://github.com/Ulthran/sbx_seeker/actions/workflows/tests.yml)
[![Super-Linter](https://github.com/Ulthran/sbx_seeker/actions/workflows/linters.yml/badge.svg)](https://github.com/Ulthran/sbx_seeker/actions/workflows/linters.yml)
<!-- Badges end -->


## Introduction

sbx_seeker is a [sunbeam](https://github.com/sunbeam-labs/sunbeam) extension for discriminating between virus and phage sequences. This pipeline uses [MEGAHIT](https://github.com/voutcn/megahit) for assembly of contigs and [seeker](https://github.com/gussow/seeker) for virus/phage discrimination.

N.B. If using Megahit for assembly, this extension requires also having sbx_assembly installed.

### Installation

```
sunbeam extend https://github.com/Ulthran/sbx_seeker.git
```

## Running

Run with sunbeam on the target `all_seeker`,

```
sunbeam run --profile /path/to/project/ all_seeker
```

### Options for config.yml

There are currently no config options for this extension.

## Legacy Installation

```
git clone https://github.com/Ulthran/sbx_seeker.git extensions/sbx_seeker
cd extensions/sbx_seeker
cat config.yml >> /path/to/sunbeam_config.yml
```

## Issues with pipeline

Please post any issues with this extension [here](https://github.com/Ulthran/sbx_seeker/issues).

