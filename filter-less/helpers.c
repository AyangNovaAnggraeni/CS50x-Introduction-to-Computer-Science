#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
   for(int i= 0; i < height; i++)
   {
        for(int j = 0; j < width; j++)
        {
            int avg = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
   }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i= 0; i < height; i++)
   {
        for(int j = 0; j < width; j++)
        {

            int sepiaRed = 0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue;
              if(sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            int sepiaGreen = 0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue;
             if(sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            int sepiaBlue = 0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue;
              if(sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
   }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i= 0; i < height; i++)
   {
        //ddb
        for(int j = 0; j < width / 2; j++)
        {
           RGBTRIPLE tmp = image[i][j];
           image[i][j] = image[i][width - 1 - j];
           image[i][width - 1 - j] = tmp;
        }
   }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];

            int pixel;
            if( i - 1 >= 0 && j - 1 >= 0 && pixel = 9)
            {
                int avg = (image([i-1],[j-1]) + image([i-1],[j+1]) + image([i+1],[j-1]) + image([i+1],[j+1]) +
                image[i - 1] + image [ i + 1] + image [j - 1] + image [j + 1] + image[i][j]) / 9;
            }
            else if (i - 1 >= 0 && j - 1 >= 0 pixel < 9)
            {
                int avg = image[pixel][pixel] / pixel;
            }

           int avg =  image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue / 3;

        }
    }
    return;
}
