using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace WindowsFormsApp8
{
    public partial class Form1 : Form
    {
        int[] a = new int[1000];
    public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            int i, n;
            string spisok;
            spisok = "";
            n = Convert.ToInt32(textBox1.Text);
            listBox1.Text = "";
            label3.Text = "";
            label4.Text = "";
            for (i = 1; i <= n; i++)
            {
                a[i] =
               Convert.ToInt32(Microsoft.VisualBasic.Interaction.InputBox("Ai=", "Enter
               array", ""));
               
                listBox1.Items.Add(a[i]);
                spisok = spisok + Convert.ToString(i) + ") " +
               Convert.ToString(a[i]) + " " + Environment.NewLine;
            }
            label7.Text = spisok;
        }
        private void label2_Click(object sender, EventArgs e)
        {
            int i, n;
            double s, sr;
            n = Convert.ToInt32(textBox1.Text);
            s = 0;
            for (i = 1; i <= n; i++) { s = s + a[i]; }
            sr = s / n;
            label3.Text = "Сумма элементов массива = " +
           Convert.ToString(s);
            label4.Text = "Ср.ар. значение = " +
           Convert.ToString(sr);
        }
    }
} 
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
        int[] a = new int[1000];
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            int n, i;
            string spisok;
            spisok = "";
            a = new int[1000];
            listBox1.Items.Clear();
            label4.Text = "";
            n = Convert.ToInt32(textBox2.Text);
            listBox1.Text = "";
            label6.Text = "Сумма элементов массива: ";
            label7.Text = "Ср. значение: ";
            for (i = 1; i <= n; i++)
            {
                a[i] =
               Convert.ToInt32(Microsoft.VisualBasic.Interaction.InputBox("Ai=", "Enter array", ""));
               
                listBox1.Items.Add(a[i]);
                spisok = spisok + Convert.ToString(i) + ") " +
               Convert.ToString(a[i]) + " " + Environment.NewLine; // перевод строки
            }
            label4.Text = spisok;

        }
        private void label5_Click(object sender, EventArgs e)
        {
            int i, n;
            double s, sr;
            n = Convert.ToInt32(textBox2.Text);
            s = 0;
            for (i = 1; i <= n; i++) { if (i % 2 != 0) s = s + a[i]; }
            sr = s / n;
            label6.Text += Convert.ToString(s);
            label7.Text += Convert.ToString(sr);
        }
    }
}