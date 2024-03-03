# c4-table

A utility to extract the issue links for a particular contest submitted by a particular user. Generates a markdown table with the issue links.

This tool can be used to make a table of your own submitted findings once the backstage access of the contest has opened and you have access to the issue links to prepare for PJQA. This can also be used to extract submissions from top auditors and read them while waiting for PJQA. This is very useful, since for contests with a large number of submissions, the github UI does not show the entire list, and one needs to search manually and note down the issue numbers.

This script uses `gh` (github cli tool) to access the backstage. Make sure you have `gh` installed and logged in.

## Installation

The tool accesses the code4rena backstage with the github cli. You need to have `gh` installed, and logged in with an account which has backstage access.

### `gh` installation

For Debian,

```bash
sudo apt-get install gh
```

For other platforms, check installation instructions [here](https://github.com/cli/cli).

### `gh` login

Must login to a github account which has backstage access with `gh`.

```bash
gh auth login
```

Follow instructions to login. For more help, check the [official documentation](https://cli.github.com/manual/gh_auth_login).

## Usage

Run with `-h` for help. Program needs 2 arguments: a contest link and a username.

Contest link can be:

1. http link of the contest findings repo
2. Name of the contest repo
3. Name of the contest findings repo

## Example usage

### With http link

```bash
c4-table https://github.com/code-423n4/2023-10-zksync-findings xuwinnie
```

### With repo name

```bash
c4-table 2023-07-tapioca GalloDaSballo
```

### With findings repo name

```bash
c4-table 2024-02-hydradx-findings carrotsmuggler
```

### Output

| Num |                                 URL                                 | Acceptance | Uniqueness | Comments |
| :-: | :-----------------------------------------------------------------: | :--------: | :--------: | -------- |
| 926 | https://github.com/code-423n4/2023-08-chainlink-findings/issues/926 |            |            |          |
| 927 | https://github.com/code-423n4/2023-08-chainlink-findings/issues/927 |            |            |          |

Columns have been named name as per my convenience. You can edit the code to change the column names/number.

### Support

If you like this tool please let me know [here]() by giving me a reaction 👍 👎 ❤️ 👀

This work was inspired from c4-stats by @one-hundred-proof. Check it out [here](https://github.com/one-hundred-proof/c4-stats)
