namespace SquizApp
{
    partial class ManualModeForm
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
            testQNADropdownLabel = new Label();
            testQNADropdownComboBox = new ComboBox();
            testQNAStartRangeNumericUpDown = new NumericUpDown();
            testQNAEndRangeNumericUpDown = new NumericUpDown();
            useTestQNACheckBox = new CheckBox();
            qnaDropdownLabel = new Label();
            qnaDropdownComboBox = new ComboBox();
            qnaStartRangeNumericUpDown = new NumericUpDown();
            qnaEndRangeNumericUpDown = new NumericUpDown();
            startRangeLabel = new Label();
            endRangeLabel = new Label();
            startQuizButton = new Button();
            squizSetupProgressBar = new ProgressBar();
            ((System.ComponentModel.ISupportInitialize)testQNAStartRangeNumericUpDown).BeginInit();
            ((System.ComponentModel.ISupportInitialize)testQNAEndRangeNumericUpDown).BeginInit();
            ((System.ComponentModel.ISupportInitialize)qnaStartRangeNumericUpDown).BeginInit();
            ((System.ComponentModel.ISupportInitialize)qnaEndRangeNumericUpDown).BeginInit();
            SuspendLayout();
            // 
            // testQNADropdownLabel
            // 
            testQNADropdownLabel.AutoSize = true;
            testQNADropdownLabel.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            testQNADropdownLabel.Location = new Point(39, 79);
            testQNADropdownLabel.Name = "testQNADropdownLabel";
            testQNADropdownLabel.Size = new Size(74, 21);
            testQNADropdownLabel.TabIndex = 7;
            testQNADropdownLabel.Text = "Test QNA";
            // 
            // testQNADropdownComboBox
            // 
            testQNADropdownComboBox.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            testQNADropdownComboBox.FormattingEnabled = true;
            testQNADropdownComboBox.Items.AddRange(new object[] { "MockQNA1", "MockQNA2", "Gregoire", "TestLatexSnippetLogic" });
            testQNADropdownComboBox.Location = new Point(135, 71);
            testQNADropdownComboBox.Name = "testQNADropdownComboBox";
            testQNADropdownComboBox.Size = new Size(502, 29);
            testQNADropdownComboBox.TabIndex = 8;
            // 
            // testQNAStartRangeNumericUpDown
            // 
            testQNAStartRangeNumericUpDown.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            testQNAStartRangeNumericUpDown.Location = new Point(671, 71);
            testQNAStartRangeNumericUpDown.Name = "testQNAStartRangeNumericUpDown";
            testQNAStartRangeNumericUpDown.Size = new Size(74, 29);
            testQNAStartRangeNumericUpDown.TabIndex = 9;
            // 
            // testQNAEndRangeNumericUpDown
            // 
            testQNAEndRangeNumericUpDown.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            testQNAEndRangeNumericUpDown.Location = new Point(770, 71);
            testQNAEndRangeNumericUpDown.Name = "testQNAEndRangeNumericUpDown";
            testQNAEndRangeNumericUpDown.Size = new Size(74, 29);
            testQNAEndRangeNumericUpDown.TabIndex = 10;
            // 
            // useTestQNACheckBox
            // 
            useTestQNACheckBox.AutoSize = true;
            useTestQNACheckBox.Location = new Point(876, 78);
            useTestQNACheckBox.Name = "useTestQNACheckBox";
            useTestQNACheckBox.Size = new Size(97, 19);
            useTestQNACheckBox.TabIndex = 11;
            useTestQNACheckBox.Text = "Use Test QNA";
            useTestQNACheckBox.UseVisualStyleBackColor = true;
            // 
            // qnaDropdownLabel
            // 
            qnaDropdownLabel.AutoSize = true;
            qnaDropdownLabel.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            qnaDropdownLabel.Location = new Point(39, 133);
            qnaDropdownLabel.Name = "qnaDropdownLabel";
            qnaDropdownLabel.Size = new Size(80, 21);
            qnaDropdownLabel.TabIndex = 12;
            qnaDropdownLabel.Text = "QNA Type";
            // 
            // qnaDropdownComboBox
            // 
            qnaDropdownComboBox.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            qnaDropdownComboBox.FormattingEnabled = true;
            qnaDropdownComboBox.Items.AddRange(new object[] { "MockQNA1", "MockQNA2", "Gregoire", "TestLatexSnippetLogic" });
            qnaDropdownComboBox.Location = new Point(135, 130);
            qnaDropdownComboBox.Name = "qnaDropdownComboBox";
            qnaDropdownComboBox.Size = new Size(502, 29);
            qnaDropdownComboBox.TabIndex = 13;
            // 
            // qnaStartRangeNumericUpDown
            // 
            qnaStartRangeNumericUpDown.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            qnaStartRangeNumericUpDown.Location = new Point(671, 130);
            qnaStartRangeNumericUpDown.Name = "qnaStartRangeNumericUpDown";
            qnaStartRangeNumericUpDown.Size = new Size(74, 29);
            qnaStartRangeNumericUpDown.TabIndex = 14;
            // 
            // qnaEndRangeNumericUpDown
            // 
            qnaEndRangeNumericUpDown.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            qnaEndRangeNumericUpDown.Location = new Point(770, 130);
            qnaEndRangeNumericUpDown.Name = "qnaEndRangeNumericUpDown";
            qnaEndRangeNumericUpDown.Size = new Size(74, 29);
            qnaEndRangeNumericUpDown.TabIndex = 15;
            // 
            // startRangeLabel
            // 
            startRangeLabel.AutoSize = true;
            startRangeLabel.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            startRangeLabel.Location = new Point(671, 27);
            startRangeLabel.Name = "startRangeLabel";
            startRangeLabel.Size = new Size(42, 21);
            startRangeLabel.TabIndex = 16;
            startRangeLabel.Text = "Start";
            // 
            // endRangeLabel
            // 
            endRangeLabel.AutoSize = true;
            endRangeLabel.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            endRangeLabel.Location = new Point(770, 27);
            endRangeLabel.Name = "endRangeLabel";
            endRangeLabel.Size = new Size(36, 21);
            endRangeLabel.TabIndex = 17;
            endRangeLabel.Text = "End";
            // 
            // startQuizButton
            // 
            startQuizButton.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            startQuizButton.Location = new Point(135, 201);
            startQuizButton.Name = "startQuizButton";
            startQuizButton.Size = new Size(244, 64);
            startQuizButton.TabIndex = 18;
            startQuizButton.Text = "Start Quiz!";
            startQuizButton.UseVisualStyleBackColor = true;
            // 
            // squizSetupProgressBar
            // 
            squizSetupProgressBar.Location = new Point(135, 306);
            squizSetupProgressBar.Name = "squizSetupProgressBar";
            squizSetupProgressBar.Size = new Size(718, 23);
            squizSetupProgressBar.TabIndex = 19;
            // 
            // ManualModeForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1050, 637);
            Controls.Add(squizSetupProgressBar);
            Controls.Add(startQuizButton);
            Controls.Add(endRangeLabel);
            Controls.Add(startRangeLabel);
            Controls.Add(qnaEndRangeNumericUpDown);
            Controls.Add(qnaStartRangeNumericUpDown);
            Controls.Add(qnaDropdownComboBox);
            Controls.Add(qnaDropdownLabel);
            Controls.Add(useTestQNACheckBox);
            Controls.Add(testQNAEndRangeNumericUpDown);
            Controls.Add(testQNAStartRangeNumericUpDown);
            Controls.Add(testQNADropdownComboBox);
            Controls.Add(testQNADropdownLabel);
            Name = "ManualModeForm";
            Text = "ManualModeForm";
            ((System.ComponentModel.ISupportInitialize)testQNAStartRangeNumericUpDown).EndInit();
            ((System.ComponentModel.ISupportInitialize)testQNAEndRangeNumericUpDown).EndInit();
            ((System.ComponentModel.ISupportInitialize)qnaStartRangeNumericUpDown).EndInit();
            ((System.ComponentModel.ISupportInitialize)qnaEndRangeNumericUpDown).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label testQNADropdownLabel;
        private ComboBox testQNADropdownComboBox;
        private NumericUpDown testQNAStartRangeNumericUpDown;
        private NumericUpDown testQNAEndRangeNumericUpDown;
        private CheckBox useTestQNACheckBox;
        private Label qnaDropdownLabel;
        private ComboBox qnaDropdownComboBox;
        private NumericUpDown qnaStartRangeNumericUpDown;
        private NumericUpDown qnaEndRangeNumericUpDown;
        private Label startRangeLabel;
        private Label endRangeLabel;
        private Button startQuizButton;
        private ProgressBar squizSetupProgressBar;
    }
}