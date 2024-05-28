.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-description.rst
|EX-CONTRIBUTING-LOGO|

*******
GitHub
*******

|tinkerer| |Engineer|

.. sidebar::

   .. contents:: On this page
      :depth: 1
      :local:

While you don't need to be an expert, you should have some knowledge about Git and GitHub, as we manage all of our code and documentation there.

All development and documentation related repositories are located in the `DCC-EX GitHub organisation <https://github.com/DCC-EX>`_.

Depending on the editing platform of your choice, you may get all the Git functionality you need, however you may optionally want to install GitHub Desktop or Sourcetree for getting a good idea on the state of the various |DCC-EX| repositories.

Code contribution process
==========================

When contributing any code to any of our repositories, no matter if you're a direct |DCC-EX| team member or an external contributor, we ask that you abide by Git best practice which is to:

1. Create a fork of the appropriate repository (only required for external contributors, team members skip this step).
2. Create a branch for all new features, bug fixes, or other updates; please don't work directly on main/master branches.
3. Save and commit your work regularly and push commits to GitHub.
4. Test your changes.
5. When you believe your code is ready, submit a pull request for the team to review.

GitHub account
===============

To start with, you will of course require an account on GitHub. If you have one already for your own personal projects, or contributing to other projects, you can simply use this. There is no need to have multiple GitHub accounts.

If you don't have one at all, then you'll need to `sign up <https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home>`_.

Git terms: fork, branch, pull request, and merge
=================================================

If you're brand new to using Git and GitHub, you will no doubt be instantly confused by four terms commonly used by Git users; fork, branch, pull request, and merge.

If you're not familiar with these, we provide a very brief overview below, however we highly recommend reading GitHub's documentation: `Collaborate with pull requests <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests>`_.

Fork
----

Yes, a fork is an implement you use to eat, but in the context of Git and GitHub, it is more akin to a fork in the road.

A fork in Git is a complete copy of a code repository created in your own Git account, however it is still linked to the original, meaning any development against this local fork can still be pushed back into the originating source repository.

If you are not a member of the |DCC-EX| team, you won't have permissions to create branches or pull requests directly against the |DCC-EX| repositories, and instead you will need to create a fork of these first.

Branch
------

When working on any new features or bug fixes, a good practice is to create a new branch prior to making any changes.

By following this practise and ensuring a new branch is created, you will always have a way to back out any changes you have made that may introduce bugs or break code, and also allows for a more collaborative approach to developing software.

Further to this, it affords an opportunity to have other contributors review your code prior to merging it in to the main code base to ensure we only release quality code.

Pull request
------------

When you're ready to get the changes made in your branch merged in to the main code base, you need to submit a pull request.

When a pull request is submitted, GitHub will automatically compare it to the main code base and advise if there are any conflicts that need to be resolved prior to merging the code, or if it is safe to proceed.

This is the point where another team member can review your proposed changes and approve or reject the request.

Merge
-----

Once a pull request is approved, it needs to be merged into the main code base.

This process will take all changes made in the files associated with the pull request and merge those into the existing files, or create/delete files as appropriate.

Note that a merge cannot be completed if there are any conflicts associated with a pull request, and they will need to be resolved first.
