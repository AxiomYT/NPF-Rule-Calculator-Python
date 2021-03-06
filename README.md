<!-- PROJECT LOGO -->
<br/>
<p align="center">
  <a href="https://github.com/AxiomYT/NPF-Rule-Calculator-Python">
    <img src="logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">NPF Rule Calculator</h3>

  <p align="center">
    A useful Astrophotography application to find the ideal exposure time, correcting for planetary shift.
    <br/>
    <br/>
    ·
    <a href="https://github.com/AxiomYT/NPF-Rule-Calculator-Python/issues">Report Bug</a>
    ·
    <a href="https://github.com/AxiomYT/NPF-Rule-Calculator-Python/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#built-with">Built With</a>
    </li>
    <li><a href="#to-do">To-Do</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


### Built With

* [ConfigParser 4.1](https://docs.python.org/3/library/configparser.html)
* [PathLib](https://docs.python.org/3/library/pathlib.html)

<!-- TO-DO -->
## To-Do

* ~~Make the calculation work~~
* Unit Test
* ~~Pull from config file~~
* ~~Allow selection of pixel_pitch states~~
* ~~Incorporate Pathlib~~

<!-- GETTING STARTED -->
## Getting Started  

* To get a local copy up and running follow these simple steps.

### Prerequisites

<ul>
  <li><a href="https://www.python.org/downloads/">Python > 3.8.5 64-bit (Other versions not tested - YMMV)</a></li>
  <li><a href="https://docs.python.org/3/library/configparser.html">ConfigParser > 4.1</a></li>
  <li><a href="https://docs.python.org/3/library/pathlib.html">PathLib</a></li>
</ul>

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AxiomYT/NPF-Rule-Calculator-Python.git
   ```
2. Execute with Python3
   ```sh
   python ./astrophotography.py
   ```



<!-- USAGE EXAMPLES -->
## Usage

### Configuration

<ul> 
  <li>Before using this programme - you absolutely must edit the [<span style="color:blue">Specific Camera Variables</span>] and [<span style="color:blue">Pixel Pitch</span>] entries in the config.cfg file.</li>
</ul>

### Value Map

```python
    # F/Stop No. (Stops)
    APERTURE = 5.6

    # Millimetres (mm)
    FOCAL_LENGTH = 300
```
<ul>
  <li>APERTURE > Has to be a Float.</li>
  <li>FOCAL_LENGTH > Has to be an Int.</li>
</ul>

```python
    PIXEL_PITCH = 6.423611111111111
    PIXEL_PITCH = 

    PIXEL_WIDTH = 
    PIXEL_WIDTH = 3456
    
    PHYSICAL_WIDTH = 
    PHYSICAL_WIDTH = 22.2
```
<ul>
  <li>PIXEL_PITCH > Has to be a Float.</li>
  <li>PIXEL_WIDTH > Has to be an Int.</li>
  <li>PHYSICAL_WIDTH > Has to be a Float.</li>
</ul>

#### Pixel Pitch Differentiation

##### Know Pixel Pitch
```python 
   PIXEL_PITCH = 6.423611111111111

   PIXEL_WIDTH = 
   PHYSICAL_WIDTH = 
```

##### Don't Know Pixel Pitch
```python
   PIXEL_PITCH = 

   PIXEL_WIDTH = 3456
   PHYSICAL_WIDTH = 22.2
```
* Essentially - If you enter a manual value for pixel pitch, the programme will use this - and ignore the values for Pixel and Physical Width.

<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Axiom - [@MM7OWO](https://twitter.com/MM7OWO)

Project Link: [https://github.com/AxiomYT/NPF-Rule-Calculator-Python](https://github.com/AxiomYT/NPF-Rule-Calculator-Python)
