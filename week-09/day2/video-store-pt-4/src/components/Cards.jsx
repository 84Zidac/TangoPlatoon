import { useNavigate } from "react-router-dom";
import * as React from 'react';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ImageListItemBar from '@mui/material/ImageListItemBar';
import ListSubheader from '@mui/material/ListSubheader';
import IconButton from '@mui/material/IconButton';
import InfoIcon from '@mui/icons-material/Info';


export default function Cards(props) {
    const navigate = useNavigate();

    return (

        
        <ImageList sx={{ width: 1000, height: 500 }} cols={3} rowHeight={500}>
  {props.filmData.map((item, index) => (
    <ImageListItem key={index}>
      <img
        onClick={() => navigate(`/film/${item.imdbID}`)}
        src={`${item.Poster}?w=164&h=164&auto=format`}
        srcSet={`${item.Poster}?w=164&h=164&auto=format&dpr=2 2x`}
        alt={item.Title}
        loading="lazy"
      />
      <ImageListItemBar
            title={`${item.Title}`}
            subtitle={`(${item.Year}) ${item.Rated}`}
            actionIcon={
              <IconButton onClick={() => navigate(`/film/${item.imdbID}`)}
                sx={{ color: 'rgba(255, 255, 255, 0.54)' }}
                aria-label={`info about ${item.Title}`}
              >
                <InfoIcon />
              </IconButton>
            }
          />
    </ImageListItem>
  ))}
</ImageList>


//         <ImageList sx={{ width: 400, height: 150 }} cols={3} rowHeight={100}>

//     <ImageListItem key={props.key}>
//       <img
//         src={props.filmData.Poster}
//         srcSet={props.filmData.Poster}
//         alt={props.filmData.Title}
//         loading="lazy"
//       />
//     </ImageListItem>

// </ImageList>
    );
}

{/* <ImageList sx={{ width: 500, height: 450 }} variant="woven" cols={3} gap={8}>
  {props.allFilmData.map((item) => (
    <ImageListItem key={item.Poster}>
      <img
        src={`${item.Poster}?w=161&fit=crop&auto=format`}
        srcSet={`${item.Poster}?w=161&fit=crop&auto=format&dpr=2 2x`}
        alt={item.Title}
        loading="lazy"
      />
    </ImageListItem>
  ))}
</ImageList> */}










// <div className="inventory_item" onClick={() => navigate(`/film/${props.filmData.imdbID}`)}>
//             <h3 className="item_title">{props.filmData.Title}</h3>
//             <img src={props.filmData.Poster} />
//         </div>