# Mdbook_Chandra_deletePls.github.io
Mdbook-configuration    
[![Latest version](https://img.shields.io/crates/v/mdbook-admonish.svg)](https://crates.io/crates/mdbook-admonish)
[![docs.rs](https://img.shields.io/badge/docs-available-brightgreen)](https://tommilligan.github.io/mdbook-admonish/)

## How to deploy Mdbook 
Follow this link : https://github.com/rust-lang/mdBook/wiki/Automated-Deployment%3A-GitHub-Actions and see the section `GitHub Pages Deploy`

 ~~Make sure if you are making any changes or adding new chapter to use `mdbook build` command to updated the `book` folder and then push the chahges~~

Since github action is set in .github/workflow, if you see the command section, it will automatically build the book, we don't have to use the `mdbook build ` command to build the book explicitely


## Adding mdbook-admonish formating style
* official site : https://github.com/tommilligan/mdbook-admonish    
* documentation : https://tommilligan.github.io/mdbook-admonish/    
* list od directive that can be used with the syntax : https://tommilligan.github.io/mdbook-admonish/reference.html#directives
---
> we need to use these command : 

```bash
# optionally, specify a directory where CSS files live, relative to the book root
mdbook-admonish install --css-dir . {directory where book.toml file is present, in place of . we can also specify folder 'asset/css }

# And below entries in the book.toml file will already be filled 
    
    [preprocessor]
    [preprocessor.admonish]
    command = "mdbook-admonish"
    assets_version = "2.0.2" # do not edit: managed by `mdbook-admonish install`

> this will generate a css file (mdbook-admonish.css)
# Once this is done, we need to point inside the book.toml file
    additional-css = ["./mdbook-admonish.css"]

```


