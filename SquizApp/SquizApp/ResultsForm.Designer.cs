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
            failedQNALoggingProgressBar = new ProgressBar();
            loggingStatusLabel = new Label();
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
            backToMainFormButton.Location = new Point(123, 139);
            backToMainFormButton.Name = "backToMainFormButton";
            backToMainFormButton.Size = new Size(283, 50);
            backToMainFormButton.TabIndex = 2;
            backToMainFormButton.TabStop = false;
            backToMainFormButton.Text = "Back to Main Page";
            backToMainFormButton.UseVisualStyleBackColor = true;
            backToMainFormButton.Click += backToMainFormButton_Click;
            // 
            // failedQNALoggingProgressBar
            // 
            failedQNALoggingProgressBar.Location = new Point(123, 335);
            failedQNALoggingProgressBar.Name = "failedQNALoggingProgressBar";
            failedQNALoggingProgressBar.Size = new Size(432, 23);
            failedQNALoggingProgressBar.TabIndex = 11;
            // 
            // loggingStatusLabel
            // 
            loggingStatusLabel.AutoSize = true;
            loggingStatusLabel.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            loggingStatusLabel.Location = new Point(123, 295);
            loggingStatusLabel.Name = "loggingStatusLabel";
            loggingStatusLabel.Size = new Size(0, 21);
            loggingStatusLabel.TabIndex = 12;
            // 
            // ResultsForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(907, 530);
            Controls.Add(loggingStatusLabel);
            Controls.Add(failedQNALoggingProgressBar);
            Controls.Add(backToMainFormButton);
            Controls.Add(amountCorrectFirstTryTextBox);
            Controls.Add(amountCorrectFirstTryLabel);
            Name = "ResultsForm";
            Text = "ResultsForm";
            Load += ResultsForm_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label amountCorrectFirstTryLabel;
        private TextBox amountCorrectFirstTryTextBox;
        private Button backToMainFormButton;
        private ProgressBar failedQNALoggingProgressBar;
        private Label loggingStatusLabel;
    }
}