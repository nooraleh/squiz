namespace SquizApp
{
    partial class CompareAnswerForm
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
            questionLabel = new Label();
            modelAnswerLabel = new Label();
            modelAnswerTextBox = new TextBox();
            userAnswerTextBox = new TextBox();
            userAnswerLabel = new Label();
            userHappyButton = new Button();
            userNotHappyButton = new Button();
            SuspendLayout();
            // 
            // questionLabel
            // 
            questionLabel.AutoSize = true;
            questionLabel.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            questionLabel.Location = new Point(33, 27);
            questionLabel.Name = "questionLabel";
            questionLabel.Size = new Size(193, 25);
            questionLabel.TabIndex = 1;
            questionLabel.Text = "Question Placeholder";
            // 
            // modelAnswerLabel
            // 
            modelAnswerLabel.AutoSize = true;
            modelAnswerLabel.Font = new Font("Segoe UI", 18F, FontStyle.Regular, GraphicsUnit.Point, 0);
            modelAnswerLabel.Location = new Point(33, 311);
            modelAnswerLabel.Name = "modelAnswerLabel";
            modelAnswerLabel.Size = new Size(167, 32);
            modelAnswerLabel.TabIndex = 2;
            modelAnswerLabel.Text = "Model Answer";
            // 
            // modelAnswerTextBox
            // 
            modelAnswerTextBox.Font = new Font("Segoe UI", 15.75F, FontStyle.Regular, GraphicsUnit.Point, 0);
            modelAnswerTextBox.Location = new Point(33, 383);
            modelAnswerTextBox.Multiline = true;
            modelAnswerTextBox.Name = "modelAnswerTextBox";
            modelAnswerTextBox.Size = new Size(563, 490);
            modelAnswerTextBox.TabIndex = 3;
            // 
            // userAnswerTextBox
            // 
            userAnswerTextBox.Font = new Font("Segoe UI", 15.75F, FontStyle.Regular, GraphicsUnit.Point, 0);
            userAnswerTextBox.Location = new Point(962, 383);
            userAnswerTextBox.Multiline = true;
            userAnswerTextBox.Name = "userAnswerTextBox";
            userAnswerTextBox.Size = new Size(527, 490);
            userAnswerTextBox.TabIndex = 5;
            // 
            // userAnswerLabel
            // 
            userAnswerLabel.AutoSize = true;
            userAnswerLabel.Font = new Font("Segoe UI", 18F, FontStyle.Regular, GraphicsUnit.Point, 0);
            userAnswerLabel.Location = new Point(962, 311);
            userAnswerLabel.Name = "userAnswerLabel";
            userAnswerLabel.Size = new Size(145, 32);
            userAnswerLabel.TabIndex = 4;
            userAnswerLabel.Text = "Your Answer";
            // 
            // userHappyButton
            // 
            userHappyButton.AutoSize = true;
            userHappyButton.Location = new Point(152, 929);
            userHappyButton.Name = "userHappyButton";
            userHappyButton.Size = new Size(211, 48);
            userHappyButton.TabIndex = 6;
            userHappyButton.Text = "I'm happy with my answer";
            userHappyButton.UseVisualStyleBackColor = true;
            userHappyButton.Click += userHappyButton_Click;
            // 
            // userNotHappyButton
            // 
            userNotHappyButton.AutoSize = true;
            userNotHappyButton.Location = new Point(1098, 935);
            userNotHappyButton.Name = "userNotHappyButton";
            userNotHappyButton.Size = new Size(235, 42);
            userNotHappyButton.TabIndex = 7;
            userNotHappyButton.Text = "I'm not happy with my answer";
            userNotHappyButton.UseVisualStyleBackColor = true;
            userNotHappyButton.Click += userNotHappyButton_Click;
            // 
            // CompareAnswerForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1698, 1025);
            Controls.Add(userNotHappyButton);
            Controls.Add(userHappyButton);
            Controls.Add(userAnswerTextBox);
            Controls.Add(userAnswerLabel);
            Controls.Add(modelAnswerTextBox);
            Controls.Add(modelAnswerLabel);
            Controls.Add(questionLabel);
            Name = "CompareAnswerForm";
            Text = "CompareAnswer";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label questionLabel;
        private Label modelAnswerLabel;
        private TextBox modelAnswerTextBox;
        private TextBox userAnswerTextBox;
        private Label userAnswerLabel;
        private Button userHappyButton;
        private Button userNotHappyButton;
    }
}