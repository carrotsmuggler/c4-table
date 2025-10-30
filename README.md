# c4-table

A utility to extract the submission links for a particular contest submitted by a particular user. Generates a markdown table with the submission links.

This tool can be used to make a table of your own submitted findings once you have access to the contest submissions, and to extract submissions from top auditors for review.

This script requires a Code4rena session cookie set in the environment variable `C4AUTH_LOGIN`.

## Setup

Set the `C4AUTH_LOGIN` environment variable to your Code4rena session cookie value.

Steps to obtain:
- Log in to the Code4rena website in your browser
- Read the `C4AUTH-LOGIN` cookie using a cookie editor or via Dev Tools -> Application -> Storage -> Cookies
- Export it: `export C4AUTH_LOGIN=...`

## Usage

Run with `-h` for help. Program needs 2 arguments: a contest reference and a username (optional for some cases).

Contest reference can be:

1. Code4rena contest URL: `https://code4rena.com/audits/2025-06-chainlink-rewards`
2. Contest slug: `2025-06-chainlink-rewards`

## Example usage

```bash
c4-table 2025-06-chainlink-rewards random1106
```

### Output

`c4-table 2025-06-chainlink-rewards random1106`

| Num | URL | Severity | Status | Occurences | Title |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 4 | https://code4rena.com/contests/2025-06-chainlink-rewards/submissions/4 | M | P | 8 | Prefix-only validation of BatchedRangeProofContext lets attackers smuggle unc... |
| 26 | https://code4rena.com/contests/2025-06-chainlink-rewards/submissions/26 | H | P | 5 | Authority Bypass in ZK Proof Context State Creation Enables Unauthorized Oper... |
| 88 | https://code4rena.com/contests/2025-06-chainlink-rewards/submissions/88 | M | P | 3 | Ignored Padding Commitment in Range Proof Allows Proof Malleability |

Found 3 submissions from random1106 in 2025-06-chainlink-rewards

Columns have been named name as per my convenience. You can edit the code to change the column names/number.

## Extra features

### Stat dump (-u | --user-stats)

Passing username is optional here. This dumps out the number of submissions per user of the contest.

```bash
-> c4-table 2025-06-chainlink-rewards -u
Username             | Number of submissions
-------------------- | ---------------
[...]
RICHA123             | 10 
radev_sw             | 13 
cheatc0d3            | 18 
Total 1186 submissions submitted by 385 users
```

### Support

If you like this tool please let me know [here](https://github.com/carrotsmuggler/c4-table/issues/1) by giving me a reaction 👍 👎 ❤️ 👀

This work was inspired from c4-stats by @one-hundred-proof. Check it out [here](https://github.com/one-hundred-proof/c4-stats)
