﻿namespace SquizApp
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            qnaDropdownComboBox = new ComboBox();
            qnaDropdownLabel = new Label();
            numberOfQuestionsLabel = new Label();
            numberOfQuestionsAskedNumericUpDown = new NumericUpDown();
            startQuizButton = new Button();
            ((System.ComponentModel.ISupportInitialize)numberOfQuestionsAskedNumericUpDown).BeginInit();
            SuspendLayout();
            // 
            // qnaDropdownComboBox
            // 
            qnaDropdownComboBox.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            qnaDropdownComboBox.FormattingEnabled = true;
            qnaDropdownComboBox.Items.AddRange(new object[] { "MockQNA1", "MockQNA2", "Gregoire" });
            qnaDropdownComboBox.Location = new Point(427, 88);
            qnaDropdownComboBox.Name = "qnaDropdownComboBox";
            qnaDropdownComboBox.Size = new Size(502, 29);
            qnaDropdownComboBox.TabIndex = 0;
            // 
            // qnaDropdownLabel
            // 
            qnaDropdownLabel.AutoSize = true;
            qnaDropdownLabel.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            qnaDropdownLabel.Location = new Point(211, 91);
            qnaDropdownLabel.Name = "qnaDropdownLabel";
            qnaDropdownLabel.Size = new Size(80, 21);
            qnaDropdownLabel.TabIndex = 1;
            qnaDropdownLabel.Text = "QNA Type";
            // 
            // numberOfQuestionsLabel
            // 
            numberOfQuestionsLabel.AutoSize = true;
            numberOfQuestionsLabel.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            numberOfQuestionsLabel.Location = new Point(211, 149);
            numberOfQuestionsLabel.Name = "numberOfQuestionsLabel";
            numberOfQuestionsLabel.Size = new Size(160, 21);
            numberOfQuestionsLabel.TabIndex = 2;
            numberOfQuestionsLabel.Text = "Number of Questions";
            // 
            // numberOfQuestionsAskedNumericUpDown
            // 
            numberOfQuestionsAskedNumericUpDown.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            numberOfQuestionsAskedNumericUpDown.Location = new Point(427, 147);
            numberOfQuestionsAskedNumericUpDown.Name = "numberOfQuestionsAskedNumericUpDown";
            numberOfQuestionsAskedNumericUpDown.Size = new Size(120, 29);
            numberOfQuestionsAskedNumericUpDown.TabIndex = 3;
            // 
            // startQuizButton
            // 
            startQuizButton.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            startQuizButton.Location = new Point(303, 307);
            startQuizButton.Name = "startQuizButton";
            startQuizButton.Size = new Size(244, 64);
            startQuizButton.TabIndex = 4;
            startQuizButton.Text = "Start Quiz!";
            startQuizButton.UseVisualStyleBackColor = true;
            startQuizButton.Click += startQuizButton_Click;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1171, 702);
            Controls.Add(startQuizButton);
            Controls.Add(numberOfQuestionsAskedNumericUpDown);
            Controls.Add(numberOfQuestionsLabel);
            Controls.Add(qnaDropdownLabel);
            Controls.Add(qnaDropdownComboBox);
            Name = "MainForm";
            Text = "Squiz";
            ((System.ComponentModel.ISupportInitialize)numberOfQuestionsAskedNumericUpDown).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ComboBox qnaDropdownComboBox;
        private Label qnaDropdownLabel;
        private Label numberOfQuestionsLabel;
        private NumericUpDown numberOfQuestionsAskedNumericUpDown;
        private Button startQuizButton;
    }
}
