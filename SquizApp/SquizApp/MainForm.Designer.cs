namespace SquizApp
{
    partial class MainForm
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
            randomModeButton = new Button();
            manualModeButton = new Button();
            welcomeLabel = new Label();
            SuspendLayout();
            // 
            // randomModeButton
            // 
            randomModeButton.Location = new Point(70, 177);
            randomModeButton.Name = "randomModeButton";
            randomModeButton.Size = new Size(250, 56);
            randomModeButton.TabIndex = 0;
            randomModeButton.Text = "Random Mode";
            randomModeButton.UseVisualStyleBackColor = true;
            randomModeButton.Click += randomModeButton_Click;
            // 
            // manualModeButton
            // 
            manualModeButton.Location = new Point(426, 177);
            manualModeButton.Name = "manualModeButton";
            manualModeButton.Size = new Size(250, 56);
            manualModeButton.TabIndex = 1;
            manualModeButton.Text = "Manual Mode";
            manualModeButton.UseVisualStyleBackColor = true;
            // 
            // welcomeLabel
            // 
            welcomeLabel.AutoSize = true;
            welcomeLabel.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            welcomeLabel.Location = new Point(70, 75);
            welcomeLabel.Name = "welcomeLabel";
            welcomeLabel.Size = new Size(209, 21);
            welcomeLabel.TabIndex = 7;
            welcomeLabel.Text = "Which mode are we picking?";
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(welcomeLabel);
            Controls.Add(manualModeButton);
            Controls.Add(randomModeButton);
            Name = "MainForm";
            Text = "MainForm";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button randomModeButton;
        private Button manualModeButton;
        private Label welcomeLabel;
    }
}