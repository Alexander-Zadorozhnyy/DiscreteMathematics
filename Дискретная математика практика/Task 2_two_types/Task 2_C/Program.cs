using System;
using System.Linq;
using System.Collections.Generic;

namespace Task_2_C
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] items = { "A", "U", "C", "G" };

            var query = from i1 in items from i2 in items from i3 in items from i4 in items 
                        from i5 in items from i6 in items from i7 in items from i8 in items
                        from i9 in items from i10 in items from i11 in items from i12 in items
                        from i13 in items from i14 in items from i15 in items
                        select i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 + i11 + i12 + i13 + i14 + i15;

            string stop1 = "UAA", stop2 = "UGA", stop3 = "UAG";
            long count = 0;
            foreach (var result in query)
            {
                if (result.IndexOf(stop1) == -1 && result.IndexOf(stop2) == -1 && result.IndexOf(stop3) == -1)
                {
                    count++;
                    if (count % 500000 == 0)
                        Console.WriteLine(result);
                }
            }
            Console.WriteLine(count * 3); // 1620249447
            Console.ReadKey();
        }
    }
}
