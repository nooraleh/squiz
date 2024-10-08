﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SquizApp
{
    public partial class ImageForm : Form
    {
        public ImageForm(string pathToImage)
        {
            InitializeComponent();
            DisplayImage(pathToImage);
        }

        private void DisplayImage(string pathToImage)
        {
            qnaPictureBox.Image = Image.FromFile(pathToImage);
        }
    }
}
