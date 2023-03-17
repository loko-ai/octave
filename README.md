<html><p><a href="https://loko-ai.com/" target="_blank" rel="noopener"> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/30443495/196493267-c328669c-10af-4670-bbfa-e3029e7fb874.png" width="8%" align="left" /> </a></p>
<h1>Octave</h1><br></html>

The **Octave** extension allows to integrate your workflows using GNU Octave functionalities. 

You can drag and drop the **Octave** component into your flow and insert your code:
<p align="center">
<img src="https://user-images.githubusercontent.com/30443495/225944366-edba9433-9531-4350-9a1b-c801057cdab8.png" width="80%" />
</p>

Variable **data** represents data received in input, while **ret** represents the output of the component.

<p align="center">
<img src="https://user-images.githubusercontent.com/30443495/225945068-eace44ba-2d29-4bba-9acf-5469293d2c72.png" width="80%" />
</p>

## Install packages

You can install new packages directly from your block:

```
pkg install -forge nan;
pkg load nan;

ret = quantile(data, .99)
```

Or you can add new packages to the *requirements_octave.txt*:
```
statistics
control
...
```
In this case, you can reuse the package as many times as you need.

## Configuration

In the file *config.json* you can mount your data volume in order to read/write files using the **Octave** block:

```
{
  "main": {
    "volumes": [
      "/home/user/loko/data:/data"
      ]
  }
}
```

