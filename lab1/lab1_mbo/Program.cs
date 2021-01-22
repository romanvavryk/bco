using System;
using LpSolveDotNet;

namespace lab1_mbo
{
    public class Solver
    {
        public double FirstValue { get; set; }
        public double SecondValue { get; set; }
        public double ThirdValue { get; set; }
        public Solver()
        {
            LpSolve.Init();
        }

        public int Solve()
        {
            int Ncol = 5;
            using (LpSolve lp = LpSolve.make_lp(0, Ncol))
            {
                if (lp == null)
                {
                    return 1;
                }
                lp.set_col_name(1, "x1");
                lp.set_col_name(2, "x2");
                lp.set_col_name(3, "x3");
                lp.set_col_name(4, "x4");
                lp.set_col_name(5, "x5");
                int[] colno = new int[Ncol];
                double[] row = new double[Ncol];

                lp.set_add_rowmode(true);
                Limit(lp, colno, row);

                int j = 0;
                colno[j] = 1; row[j++] = 2;
                colno[j] = 2; row[j++] = 3;
                colno[j] = 3; row[j++] = 1;
                colno[j] = 4; row[j++] = 2;
                colno[j] = 5; row[j++] = 0;
                if (lp.add_constraintex(j, row, colno, lpsolve_constr_types.GE, 8) == false)
                {
                    return 3;
                }

                j = 0;
                colno[j] = 1; row[j++] = 3;
                colno[j] = 2; row[j++] = -1;
                colno[j] = 3; row[j++] = 0;
                colno[j] = 4; row[j++] = 0;
                colno[j] = 5; row[j++] = 0;
                if (lp.add_constraintex(j, row, colno, lpsolve_constr_types.GE, 6) == false)
                {
                    return 3;
                }

                lp.set_add_rowmode(false);

                j = 0;
                colno[j] = 1; row[j++] = 1;
                colno[j] = 2; row[j++] = -4;
                colno[j] = 3; row[j++] = 0;
                colno[j] = 4; row[j++] = 0;
                colno[j] = 5; row[j++] = 0;
                if (lp.set_obj_fnex(j, row, colno) == false)
                {
                    return 4;
                }

                lp.set_minim();
                lp.write_lp("MainComponent/MainComponent_First.lp");

                lp.set_verbose(lpsolve_verbosity.IMPORTANT);

                lpsolve_return s = lp.solve();
                if (s != lpsolve_return.OPTIMAL)
                {
                    return 5;
                }

                lp.get_variables(row);
                for (j = 0; j < Ncol; j++)
                {
                    Console.WriteLine("\t" + lp.get_col_name(j + 1) + $": {row[j]:0.00}" + "; ");
                }
                Console.WriteLine($"\tResult is: {lp.get_objective():0.00}");
                System.Console.WriteLine();
            }
            return 0;
        }

        public static int Limit(LpSolve lp, int[] colno, double[] row)
        {

            int j = 0;
   
            colno[j] = 1; row[j++] = 1;
            colno[j] = 2; row[j++] = 2;
            colno[j] = 3; row[j++] = 1;
            colno[j] = 4; row[j++] = 0;
            colno[j] = 5; row[j++] = 0;
            if (lp.add_constraintex(j, row, colno, lpsolve_constr_types.EQ, 6) == false)
            {
                return 3;
            }

       
            j = 0;
            colno[j] = 1; row[j++] = 2;
            colno[j] = 2; row[j++] = 1;
            colno[j] = 3; row[j++] = 0;
            colno[j] = 4; row[j++] = 1;
            colno[j] = 5; row[j++] = 0;
            if (lp.add_constraintex(j, row, colno, lpsolve_constr_types.EQ, 8) == false)
            {
                return 3;
            }


            j = 0;
            colno[j] = 1; row[j++] = -1;
            colno[j] = 2; row[j++] = 1;
            colno[j] = 3; row[j++] = 0;
            colno[j] = 4; row[j++] = 0;
            colno[j] = 5; row[j++] = 1;
            if (lp.add_constraintex(j, row, colno, lpsolve_constr_types.EQ, 4) == false)
            {
                return 3;
            }
            return 0;
        }
    }
        class Program
    {
        static void Main(string[] args)
        {
            Solver solver = new Solver();
            solver.Solve();

        }
    }
}
