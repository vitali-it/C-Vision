import React, { Fragment, useState } from 'react';
import axios from 'axios';
import './styles.css';

export const UploadContainer = () => {
    const [selectedFile, setSelectedFile] = useState();
    const [imgPlot, setImgPlot] = useState();
    const [piePlot, setPiePlot] = useState();
    const [processing, setProcessing] = useState('hidden');
    const [imgVisibility, setImgVisibility] = useState('hidden');
    const formData = new FormData(); 
    const decoder = 'data:image/png;base64,';

    const handleSubmit = async(event) => {
      event.preventDefault();
      let status = 500;
      formData.append('image', selectedFile);
      setProcessing('visible');
      try {
        await axios({
          method: 'post',
          timeout: 10000,
          url: 'http://localhost:5000/upload',
          data: formData
        }).then(res => {
          status = res.status;
          setImgPlot([decoder, res.data['img_plot']].join(''));
          setPiePlot([decoder, res.data['pie_plot']].join(''));
        }).then(() => {
          if (status === 200) {
              setImgVisibility('visible');
              setProcessing('hidden');
          }
        });
      } catch(error) {
        console.error(error);
      }
    }

    const handleInput = (event) => {
      setSelectedFile(event.target.files[0]);
    }

    const browse = () => {
      document.getElementById('image').click();
    }

    return (
      <Fragment>
          <h2>Upload an image</h2>
          <form onSubmit={handleSubmit} encType='multipart/form-data'>
              <nav className='form-container'>
                  <label onClick={browse}>Choose a picture (jpg, png)</label>
                  <input type='file' name='image' id='image' onChange={handleInput}/>
                  <button id='btn' type='submit'>Predict</button>
              </nav>
              <h2 id='imgs' style={{ visibility: processing }}>Processing !!!!!!!!!!!!!!!</h2>
              <span id='imgs' style={{ visibility: imgVisibility }} className='img-container'> 
                  <img id='img_plot' src={imgPlot} alt='Plot'/>
                  <img id='pie_plot' src={piePlot} alt='Plot'/>
              </span>
          </form>
      </Fragment>
    )
};
