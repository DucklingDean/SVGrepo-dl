from setuptools import setup, find_packages



setup(
    name             ='svg-repo-dl',
    version          ='0.0.0',
    description      ="SVGrepo-dl is a library & command-line tool for downloading SVG icons and illustrations from 'svgrepo.com'.",
    #long_description              = open('README.md', 'r').read(),
    #long_description_content_type = 'text/markdown',
    author           ='Duckling Dean',
    author_email     ='duckling.dean@proton.me',
    package_dir      ={'': 'src'},
    packages         =find_packages(where='src'),
    include_package_data=True,
    project_urls     ={
        "Source" : "https://github.com/DucklingDean/SVGrepo-dl",
    },


    #install_requires = [
    #   "requests>=2.32.2,<3.0.0",
    #   "reqio"
    # ]
)


