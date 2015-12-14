# Jim Python Naming Conventions

### Goals:
* Follow Pythonic, GitHub and other authoritative conventions as much as possible

### Conventions:

* GitHub Repo Names: short, lower-case, hyphen-separated if necessary
    * Background:
        * From .NET/Java, I'm used to using camel-case. Hard habit to break, but I think I need to:
        * [PEP8](https://www.python.org/dev/peps/pep-0008/#package-and-module-names) recommends lowercase underscore-separated: "Modules should have short, all-lowercase names. 
        Underscores can be used in the module name if it improves readability."
        * For package names (collections of modules): short, lower-case, avoid underscores.
        * PEP8 is relevant because the project directory name is the package name.
        * GitHub doesn't have an authoritative answer, but 
        [this](http://stackoverflow.com/questions/19077110/is-it-suggested-to-have-git-repository-names-in-upper-or-camel-case-instead-of-l) 
        is the closest I found. Excerpts:
        * "a good naming convention would be: use lowercase; separate word with hyphens."
    * All agree on lowercase.
    * Disagreement on underscore or hyphen. 
    * Decided: go with pythonic underscore. 
    
