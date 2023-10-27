<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kierannp/SMARTREE">
  </a>

<h3 align="center">SMARTREE</h3>

  <p align="center">
    A package for generating iterative SMARTS strings for forcefield atomtyping.
    <br />
    <a href="https://github.com/kierannp/SMARTREE"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kierannp/SMARTREE">View Demo</a>
    ·
    <a href="https://github.com/kierannp/SMARTREE/issues">Report Bug</a>
    ·
    <a href="https://github.com/kierannp/SMARTREE/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is an algorithm I made to dynamicly generate SMARTS molecule definitions for forcefield creation. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get this package up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* enviroment activation
```sh
conda env create -f enviroment.yml
conda activate SMARTREE
```

### Installation

* package installation
 ```sh
  git clone https://github.com/kierannp/SMARTREE.git
  cd SMARTREE
  pip install -e .
 ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```python
 import networkx as nx
 import mbuild as mb
 import sTree

 smiles = "C(CO)NCCO" # Diethanolamine

 mol = mb.load(smiles, smiles=True) # converts the smiles into a mb.Compound

 BG = mol.bond_graph # the bond graph of our molecule, atoms connected by bonds represented as a Set of source atom to destination atoms

 depth = 2 # this parameter determines how large the smart tree should be generated, the larger the depth the more specific your SMARTS definition is, but the more expensive it is to atomtype 
 smarts_dict = sTree.bond_graph_to_smarts_dic(BG, depth) # returns our 

```

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kieran Nehil-Puleo - nehilkieran@gmail.com

Project Link: [https://github.com/kierannp/SMARTREE](https://github.com/kierannp/SMARTREE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
