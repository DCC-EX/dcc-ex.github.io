\|EX-CONTRIBUTING-LOGO\|

# Contributing to EX-WebThrottle2

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: sidebar

::: 
On this page
:::
::::

Firstly, thank you for wanting to get involved with EX-WebThrottle2! Any
contribution, no matter how big or small, is very much appreciated!

This page should give a step by step guide to contributing, from getting
the tools you\'ll need to making the pull request. These steps are:

- Get the tools
- Read our code standards
- Make a branch
- Create commits
- Open a pull request

## Developer tools

:!!! note "::: title
Note"
:::

You may want to have a look at our page on
`/about/contributing/software` and also
our page on `/about/contributing/github`
if you\'ve never used git or GitHub before
::::

We strongly recommend using Visual Studio Code (VSCode) to work on
EX-WebThrottle2. You can download it from Microsoft\'s website
[here](https://code.visualstudio.com/) \|EXTERNAL-LINK\|. Whilst you are
waiting for it to install, you can be getting a local copy of the code.

Once you have downloaded VSCode and installed it, open VSCode then click
`File --> Open Workspace from file...` then find your local copy of the code and select
\"EX-WebThrottle2.code-workspace\". Once VSCode has loaded the
workspace, you should see a popup in the bottom right asking you if you
want to install the recommended extensions. It\'s recommended you
install these and they are:

- [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
  \|EXTERNAL-LINK\|
- [Vuetify](https://marketplace.visualstudio.com/items?itemName=vuetifyjs.vuetify-vscode)
  \|EXTERNAL-LINK\|
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
  \|EXTERNAL-LINK\|
- [Spell
  Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
  \|EXTERNAL-LINK\|

You\'ll need to set up Volar to handle TypeScript, instead of the built
in TypeScript extension. To do this, follow these steps:

1.  Open the command palette
    (`View --> Command Palette`)
2.  Run Extensions: Show Built-in Extensions command
3.  Find TypeScript and JavaScript Language Features, right click and
    select [Disable (Workspace)]
4.  Reload VSCode, and then open any vue file to trigger Volar
    activation (no longer need in 0.28.4).

Next you\'ll need to install Node.js to run the development tools.
Again, you can download it from their website
[here](https://nodejs.org/en/) \|EXTERNAL-LINK\|. We recommend you use
the LTS version of Node.

Once Node is installed, open a terminal in VSCode
(`Terminal --> New terminal`)
and run the following command to install all the dependencies:

``` shell
npm install
```

Then to run the code locally:

``` shell
npm run dev
```

### Code standards

For EX-WebThrottle2, we follow the [Google Style
Guides](https://google.github.io/styleguide/) \|EXTERNAL-LINK\|,
specifically the
[HTML/CSS](https://google.github.io/styleguide/htmlcssguide.html)
\|EXTERNAL-LINK\| and
[TypeScript](https://google.github.io/styleguide/tsguide.html)
\|EXTERNAL-LINK\| style guides. This means we use a indent of two spaces
and single quotes for strings. Also, although semicolons are optional in
JavaScript, we have configured the linter to enforce semicolons. If you
have installed the recommended extensions, VSCode should highlight
problems for you. You can also find (and fix some) problems using the
following command:

``` shell
npm run lint
```

## Development process

### Branches

Here is a summary of what different branches are used for.

#### Main branches

There are two \'main\' branches, `main` and `next-release`. These
branches can\'t be pushed to directly, instead you need to create a pull
request. `main` is the branch for the current release cycle and
`next-release` is for the next release cycle. You should only open a
pull request to `main` if you are submitting a fix for bugfix release.

#### Development branches

**Members of DCC-EX**

Branches should be named based off the feature they are for, and if
multiple people are working on the same feature, you can make branches
named `feature-name/username`. If you are developing a patch for the
current release, you can use the same naming scheme but branch from
`main` instead.

**Everyone else**

It doesn\'t really matter how you work in your fork, just make sure you
open your pull request to the right branch (discussed further down in
`about/contributing/webthrottle:opening a pull request`).

### Commits

Please make sure that when you name a commit it accurately describes the
contents of the commit and has a prefix to describe the type of the
commit. These prefixes are:

- WIP: A feature or fix that isn\'t finished yet
- Fix: a finished fix with a reference to the GitHub issue
- Feat: A finished feature
- Chore: Code maintenance such as adding comments or removing dead code

An example would be: \|BR\| *WIP: Add a new button* \|BR\| Or \|BR\|
*Fix: button now works (#52)*

If you feel able to, please consider signing your commits (See this
guide if you want to have a go: [Verified commits -
GitHub](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification)
\|EXTERNAL-LINK\|).

## Opening a pull request

Before you open a pull request, consider running the following commands:

``` shell
npm run test:unit
npm run test:e2e
```

These commands run our automated tests and should highlight if you have
broken any other code. If you can\'t or forget, don\'t worry, these will
be run when your pull request is submitted automatically.

If you have added large amounts of new functionality, it would also be
great if you could write tests to go with it, if you know how to do it.

Both `main` and `next-release` have branch protection, meaning you
can\'t push to them directly, instead you have to open a pull request.
The branch `next-release` will be used to collect features for the next
point release (major or minor), so this is the branch to base your
branches on for new features, whilst `main` is used to prepare bugfix
releases. Make sure you open a pull request to the right one!

Once you\'ve opened your pull request, one of our team will have a look
and get it merged into the code. Congratulations, you have contributed
to EX-WebThrottle2!
