Title: Pelican on GitHub Pages
Date: 2023-08-12
Category: Guides
Tags: github, python, pelican, devcontainers, vscode, docker, pages, gh-pages
Author: Ryan Squires
Summary: Make a devblog, they said.  It'll be easy, they said.

![SQUAAAAWK!]({static}/images/goofypelican.jpeg){: .image-process-article-image}

## Read the docs.  No, the other docs.

If you happen to be trying to set up a Pelican site using github pages, just [follow the Pelican docs' tips page](https://docs.getpelican.com/en/latest/tips.html). Originally, I found a link on Pelican's wiki page to an outdated guide using the [pelican-to-github-pages action](https://github.com/marketplace/actions/pelican-to-github-pages) that has fallen into disrepair. But there's good news! All of the tools you need are built into Pelican, git, and github directly. In my (many) attempts at getting that action working though, I learned a lot about [VSCode's dev containers implementation](https://code.visualstudio.com/docs/devcontainers/containers). That part of the project stuck, and I absolutely recommend giving them a shot. For extra fun, I happened to be SSHing into my burgeoning homelab's raspberry pi throughout this process, which surprisingly, thanks to VSCode's remote explorer extension, really didn't add much complexity, to my surprise. Here's a brief breakdown of how to get it all that up and running.

1. [Install Docker](https://docs.docker.com/desktop/) on all machines involved.

2. On the machine on which you want the dev container to be hosted, follow steps 1-4 [here](https://cloudbytes.dev/snippets/automate-deployment-of-pelican-website-to-github-pages) to get your Pelican dev container up and running.

3. Once that's up, [create your Github pages site repository](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages) and connect it as a remote to your local repo. I chose to make a "Project" site, meaning your main branch will contain your Pelican configs and assets, and your site's actual html will be on the gh-pages branch.

4. In your pelicanconf.py file, located in `workspaces/<gh-username>.github.io/`, make sure the following variables are set, in addition to the ones set automatically by the `pelican-autoconfig` command you ran in Step 2. Careful: here there be gotchas.

        :::python
        SITEURL = 'https://your.url.com' # either <your-username>.github.io or your custom domain
        PATH = 'content'
        OUTPUT_PATH = 'output'
        DELETE_OUTPUT_DIRECTORY = True   # possibly unnecessary, but I used it

    - If you're using a custom URL, [follow this section of the docs'](https://docs.getpelican.com/en/latest/tips.html#copy-static-files-to-the-root-of-your-site) instructions. The CNAME file should be created in `content/extras/`, and should contain your custom URL, sans http(s)://. Then, add the following to pelicanconf.py:
            
            :::python
            STATIC_PATHS = ['images', 'extra/CNAME',]
            EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

    - I also suggest setting up a [theme](https://github.com/getpelican/pelican-themes). I cloned the aforelinked repo to my devcontainer's home directory, `/home/vscode/`, as per its README, and then back in `pelicanconf.py`, added:
            
            :::python
            THEME = "/home/vscode/pelican-themes/<your-choice-of-theme>"

5. For future repo cleanliness, I added `output/`, `__pycache__/`, and `.gitignore` to a .gitignore file (create it if it doesn't exist yet) in the main branches' root directory.  This prevents the output directory from existing in both branches, which I found sometimes confused git, causing a need for multiple commits.
    - Now, follow the Pelican docs' [guide on publishing a project page to github](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github).
    - In order to do this automatically every time you commit, follow [this](https://docs.getpelican.com/en/latest/tips.html#update-your-site-on-each-commit). You may need to create the "post-commit" file it mentions (I did). If you plan on having both your project and site branches, I recommend tweaking the suggested command a bit to push both branches simultaneously: 

            :::bash 
            pelican content -o output -s pelicanconf.py && 
            ghp-import output && 
            git push --all origin

6. At this point, after github runs its github-pages action, you should have a website, available either at `<your-username>.github.io`, or the custom URL you defined earlier.

**Bonus!** Looking for an easy way to get images (or other files) onto your devcontainer? No problem! Docker to the rescue:

- First, find your devcontainer's given name on the container's host with `docker ps`. Then, fill in the blanks:

        :::bash
        docker cp /path/and/filename.jpg <container_name>:/workspaces/<ghUsername>.github.io/content/images/

- If you're hosting the devcontainer on another machine and SSH-ing in, there's an extra wrinkle:

        :::bash
        docker context create <name-of-host> --docker "host=ssh://<username>@<IP>"
        docker --context <name-of-host> cp /path/and/filename.jpg <container_name>:/workspaces/<ghUsername>.github.io/content/images/

    The `<name-of-host>` there is entirely arbitrary and just for docker's use to identify the context you're creating.

###### Now to write some content...