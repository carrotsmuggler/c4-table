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

Run with `-h` for help. Program needs 2 arguments: a contest link and a username (optional for some cases).

Contest link can be:

1. http link of the contest findings repo: `https://github.com/code-423n4/2023-10-zksync-findings`
2. Name of the contest repo: `2023-10-zksync`
3. Name of the contest findings repo: `2023-10-zksync-findings`

## Example usage

```bash
c4-table 2023-08-chainlink carrotsmuggler
```

### Output

`c4-table 2023-08-chainlink carrotsmuggler`

| Num |                                 URL                                 |                        Title                         | Acceptance | Uniqueness | Comments |
| :-: | :-----------------------------------------------------------------: | :--------------------------------------------------: | :--------: | :--------: | -------- |
| 927 | https://github.com/code-423n4/2023-08-chainlink-findings/issues/927 | Unbonding period can be constantly reset for no cost |            |            |          |
| 926 | https://github.com/code-423n4/2023-08-chainlink-findings/issues/926 |   Rewards can keep increasing even after migration   |            |            |          |

Columns have been named name as per my convenience. You can edit the code to change the column names/number.

## Extra features

### Quick links ( -l | --links-only)

Fetches only the issue urls, and not the issue titles. Very fast since all issues dont need to be fetched.

### Stat dump (-u | --user-stats)

Passing username is optional here. This dumps out the submissions per user of the contest.

```bash
-> c4-table 2024-03-neobase-findings -u
Username             | Number of issues
-------------------- | ---------------
0xsomeone            | 3
carrotsmuggler       | 4
rvierdiiev           | 5
Arabadzhiev          | 6
said                 | 6
Total issues submitted: 25
```

### Support

If you like this tool please let me know [here](https://github.com/carrotsmuggler/c4-table/issues/1) by giving me a reaction 👍 👎 ❤️ 👀

This work was inspired from c4-stats by @one-hundred-proof. Check it out [here](https://github.com/one-hundred-proof/c4-stats)
