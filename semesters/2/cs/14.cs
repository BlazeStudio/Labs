using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace Laba5_nechit
{
    public partial class Form1 : Form
    {
        int y, max, xn, xk, xmax, dx, k;

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void comboBox3_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int i;
            for (i = 1; i <= 7; i++)
            {
                comboBox1.Items.Add(Convert.ToString(i - 10));
                comboBox2.Items.Add(Convert.ToString(i + 10));
                comboBox3.Items.Add(Convert.ToString(i + 1));
            }
        }
        static int Factorial(int x)
        {
            if (x == 0) { return 1; }
            else { return x * Factorial(x - 1); }
        }


    private void button1_Click(object sender, EventArgs e)
        {
            int i;
            listBox1.Text = ""; listBox1.Items.Clear();
            xn = Convert.ToInt32(comboBox1.Text); xk = Convert.ToInt32(comboBox2.Text); dx = Convert.ToInt32(comboBox3.Text); listBox1.Text = ""; k = Convert.ToInt32(comboBox4.Text);
            max = 0;
            i = xn;
            while (i <= xk)
            {
                y = i + k;
                if ((i >= 8) && (i <= 10)) { y = Factorial(i - 7); }
                else if (i > 12 && i <= 20) { y = Factorial(i - 11); }
                if (y > max) { max = y; xmax = i; }
                listBox1.Items.Add(Convert.ToString(i) + ")	" +
                Convert.ToString(y));
                i += dx;
            }


        }

        private void label1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Y = " + Convert.ToString(y) + "	при х = " + Convert.ToString(xmax), "Результат:", MessageBoxButtons.OK,
  MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1);
        }
    }
}


