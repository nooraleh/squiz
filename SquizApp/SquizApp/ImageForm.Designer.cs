namespace SquizApp
{
    partial class ImageForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            qnaPictureBox = new PictureBox();
            ((System.ComponentModel.ISupportInitialize)qnaPictureBox).BeginInit();
            SuspendLayout();
            // 
            // qnaPictureBox
            // 
            qnaPictureBox.Dock = DockStyle.Fill;
            qnaPictureBox.Location = new Point(0, 0);
            qnaPictureBox.Name = "qnaPictureBox";
            qnaPictureBox.Size = new Size(800, 450);
            qnaPictureBox.SizeMode = PictureBoxSizeMode.AutoSize;
            qnaPictureBox.TabIndex = 0;
            qnaPictureBox.TabStop = false;
            // 
            // ImageForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(qnaPictureBox);
            Name = "ImageForm";
            Text = "ImageForm";
            ((System.ComponentModel.ISupportInitialize)qnaPictureBox).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private PictureBox qnaPictureBox;
    }
}