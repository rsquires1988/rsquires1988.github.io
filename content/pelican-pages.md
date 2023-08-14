Title: Pelican on GitHub Pages
Date: 2023-08-12
Category: Snippets
Tags: github, python, pelican, devcontainers, vscode, docker, pages, gh-pages
Author: Ryan Squires
Summary: I didn't hear no bell

<!-- ![SQUAAAAWK!]({static}/images/goofypelican.jpeg){: .image-process-article-image} -->
![SQUAAAAWK!]({static}/images/goofypelican.jpeg){: .image-process-article-image}

## Read the docs.  No, the other docs.

If you happen to be trying to set up a Pelican site using github pages, just [follow the Pelican docs' tips page](https://docs.getpelican.com/en/latest/tips.html). Originally, I found a link on Pelican's wiki page to an outdated guide using the [pelican-to-github-pages action](https://github.com/marketplace/actions/pelican-to-github-pages) that, while I think it CAN work, has fallen into disrepair and is generally more trouble than it's worth, because all of the tools you need are built into Pelican, git, and github directly. I will say though, that I learned a lot about [VSCode's dev containers implementation](https://code.visualstudio.com/docs/devcontainers/containers) along the way, and I'm pretty jazzed about that. That part of the project stuck, and I absolutely recommend giving them a shot. For extra fun, I happened to be SSHing into my burgeoning homelab's raspberry pi throughout this process, so keep in mind that some of these steps will be extraneous if you're setting this up on your local machine. Here's a brief breakdown of how to get all that up and running, the end result being your very own devblog, like this one!

1. [Install Docker](https://docs.docker.com/desktop/) on all machines involved
2. On the machine on which you want the dev container to be hosted, follow steps 1-4 [here](https://cloudbytes.dev/snippets/automate-deployment-of-pelican-website-to-github-pages) to get your Pelican dev container up and running.
3. Once that's up, [create your Github pages site repository](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages) and connect it as a remote to your local repo. I chose to make a "Project" site, although I think the distinction is somewhat moot here. For context, the final product will contain your Pelican configs and assets on the main branch, and your site's actual html on the gh-pages branch.
4. Make any changes to your pelicanconf.py file that you need to, but here there be gotchas. Make sure that your `SITEURL` variable is set to the URL you want your site to be available on.  If you intend to use a custom URL, use that here, including `https://`. `OUTPUT_PATH` should be set to `'output/'`, `PATH` to `'content'`.  I'm not entirely sure if this one was necessary or not, but I set `DELETE_OUTPUT_DIRECTORY` to `True`.  Also, if you're using a custom URL, [follow this section of the docs'](https://docs.getpelican.com/en/latest/tips.html#copy-static-files-to-the-root-of-your-site) instructions.  The `STATIC_PATHS` and `EXTRA_PATH_METADATA` variables should be set in your pelicanconf.py, and the CNAME file should be created in ./content/extras/.
    - I also suggest setting up a [theme](https://github.com/getpelican/pelican-themes). I cloned the aforelinked repo to my devcontainer's home directory, `/home/vscode/`, as per its README, and then back in `/workspaces/<your-gh-username>.github.io/pelicanconf.py`, added `THEME = /home/vscode/pelican-themes/<your-choice-of-theme>`.
5. For future repo cleanliness, I added `output/`, `__pycache__/`, and `.gitignore` to a .gitignore file (create it if it doesn't exist yet) in the main branches' root directory.  This prevents the output directory from existing in both branches, which I found sometimes confused git, which caused a need for multiple commits.
    - Now, follow the Pelican docs' [guide on publishing a project page to github](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github).
    - In order to do this automatically every time you commit, follow [this](https://docs.getpelican.com/en/latest/tips.html#update-your-site-on-each-commit). You may need to create the "post-commit" file it mentions (I did). If you plan on having both your project and site branches, I recommend tweaking the suggested command a bit: `pelican content -o output -s pelicanconf.py && ghp-import output && git push --all origin` This will push both branches simultaneously.
6. At this point, after github runs its github-pages action, you should have a website, available either at `<your-username>.github.io`, or the custom URL you defined earlier.

I probably forgot something, so if you're stuck, feel free to email me at ryan@rousebrowse.com

### Happy dotcom-ing!
