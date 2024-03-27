namespace SquizApp
{
    partial class ResultsForm
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
            amountCorrectFirstTryLabel = new Label();
            amountCorrectFirstTryTextBox = new TextBox();
            backToMainFormButton = new Button();
            SuspendLayout();
            // 
            // amountCorrectFirstTryLabel
            // 
            amountCorrectFirstTryLabel.AutoSize = true;
            amountCorrectFirstTryLabel.Location = new Point(123, 88);
            amountCorrectFirstTryLabel.Name = "amountCorrectFirstTryLabel";
            amountCorrectFirstTryLabel.Size = new Size(188, 15);
            amountCorrectFirstTryLabel.TabIndex = 0;
            amountCorrectFirstTryLabel.Text = "Amount Correct on First Attempt: ";
            // 
            // amountCorrectFirstTryTextBox
            // 
            amountCorrectFirstTryTextBox.Location = new Point(343, 85);
            amountCorrectFirstTryTextBox.Name = "amountCorrectFirstTryTextBox";
            amountCorrectFirstTryTextBox.Size = new Size(212, 23);
            amountCorrectFirstTryTextBox.TabIndex = 1;
            // 
            // backToMainFormButton
            // 
            backToMainFormButton.Font = new Font("Segoe UI", 18F, FontStyle.Regular, GraphicsUnit.Point, 0);
            backToMainFormButton.Location = new Point(232, 208);
            backToMainFormButton.Name = "backToMainFormButton";
            backToMainFormButton.Size = new Size(239, 110);
            backToMainFormButton.TabIndex = 2;
            backToMainFormButton.TabStop = false;
            backToMainFormButton.Text = "Back to Main Page";
            backToMainFormButton.UseVisualStyleBackColor = true;
            // 
            // ResultsForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(backToMainFormButton);
            Controls.Add(amountCorrectFirstTryTextBox);
            Controls.Add(amountCorrectFirstTryLabel);
            Name = "ResultsForm";
            Text = "ResultsForm";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label amountCorrectFirstTryLabel;
        private TextBox amountCorrectFirstTryTextBox;
        private Button backToMainFormButton;
    }
}