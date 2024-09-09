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
        int[] b = new int[1000];
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
                int i;
                for (i = 1; i <= 7; i++)
                {
                    comboBox1.Items.Add(Convert.ToString(i + 1));
                    comboBox2.Items.Add(Convert.ToString(i + 1));
                    comboBox3.Items.Add(Convert.ToString(i - 10));
                    comboBox4.Items.Add(Convert.ToString(i + 10));
                }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i, j, m, n, minZn, maxZn; int[,] a = new int[100, 100];


            m = Convert.ToInt32(comboBox1.Text); n = Convert.ToInt32(comboBox2.Text);
            minZn = Convert.ToInt32(comboBox3.Text); maxZn = Convert.ToInt32(comboBox4.Text);
            if (minZn > maxZn) { DialogResult result = MessageBox.Show("Ошибка! Значение MIN больше значения MAX", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Warning, MessageBoxDefaultButton.Button1); }
            else
            {
                dataGridView1.RowCount = m + 1; dataGridView1.ColumnCount = n + 1;
                dataGridView1.Width = 217 * (n + 1); dataGridView1.Height = 27 * (m + 1);

                //очистка таблицы
                for (i = 1; i <= m; i++)
                {
                    for (j = 1; j <= n; j++)
                    {
                        dataGridView1.Rows[i].Cells[j].Value = " ";
                    }
                }
                Random rnd = new Random();
                //задание элементов массива и выдача их в сетку
                    for (i = 1; i <= m; i++)
                    {
                        for (j = 1; j <= n; j++)
                        {
                            a[i, j] = rnd.Next(minZn, maxZn); dataGridView1.Rows[i].Cells[j].Value = Convert.ToString(a[i, j]);
                        }
                    }
                    //нумерация строк и столбцов
                    for (i = 1; i <= m; i++)
                    {
                        dataGridView1.Rows[i].Cells[0].Value = Convert.ToString(i);
                    }
                    for (j = 1; j <= n; j++)
                    {
                        dataGridView1.Rows[0].Cells[j].Value = Convert.ToString(j);
                    }
            }
        }

private void label6_Click(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }
    }
}


