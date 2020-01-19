import unittest
import ast
import solution
import os
print(os.getcwd())

with open('./coderbyte/solution.py') as f:
    TREE = ast.parse(f.read())
    COUNT = sum(isinstance(exp, ast.FunctionDef) for exp in TREE.body)
    print('\nThere are {} functions in solution.py\n{}'.format(COUNT, '='*70))


class Test(unittest.TestCase):

    def test_LetterChanges(self):
        self.assertEqual(solution.LetterChanges(""), "")
        self.assertEqual(solution.LetterChanges("coderbyte"), "dpEfsczUf")
        self.assertEqual(solution.LetterChanges("beautiful^"), "cfbvUjgvm^")
        self.assertEqual(solution.LetterChanges("123456789ae"), "123456789bf")
        self.assertEqual(solution.LetterChanges("a b c dee"), "b c d Eff")
        self.assertEqual(solution.LetterChanges(
            "a confusing /:sentence:/[ this is not!!!!!!!~*3"),
            "b dpOgvtjOh /:tfOUfOdf:/[ UIjt jt OpU!!!!!!!~*3")
        self.assertEqual(solution.LetterChanges("coderbyte"), "dpEfsczUf")

    def test_FirstReverse(self):
        self.assertEqual(solution.FirstReverse(" 1 Abc"), "cbA 1 ")

    def test_CorrectPath(self):
        self.assertEqual(solution.CorrectPath("???rrurdr?"), "dddrrurdrd")
        self.assertEqual(solution.CorrectPath("drdr??rrddd?"), "drdruurrdddd")
        self.assertEqual(solution.CorrectPath(
            "rd?u??dld?ddrr"), "rdrurrdldlddrr")

    def test_ScaleBalancing(self):
        self.assertEqual(solution.ScaleBalancing(
            ["[3, 4]", "[1, 2, 7, 7]"]), "1")
        self.assertEqual(solution.ScaleBalancing(
            ["[13, 4]", "[1, 2, 3, 6, 14]"]), "3,6")
        self.assertEqual(solution.ScaleBalancing(
            ["[5, 9]", "[1, 2, 6, 7]"]), "2,6")

    def test_VowelSquare(self):
        self.assertEqual(solution.VowelSquare(
            ["abcd", "eikr", "oufj"]), '1-0')
        self.assertEqual(solution.VowelSquare(
            ["aqrst", "ukaei", "ffooo"]), '1-2')
        self.assertEqual(solution.VowelSquare(["aaa", "eee"]), '0-0')
        self.assertEqual(solution.VowelSquare(["aeooo", "ffffg"]), 'not found')

    def test_ClosestEnemyII(self):
        self.assertEqual(solution.ClosestEnemyII(["000", "100", "200"]), 1)
        self.assertEqual(solution.ClosestEnemyII(
            ["0000", "2010", "0000", "2002"]), 2)

    def test_QuestionsMarks(self):
        self.assertEqual(solution.QuestionsMarks('aa6?9'), 'false')
        self.assertEqual(solution.QuestionsMarks(
            'acc?7??sss?3rr1??????5'), 'true')
        self.assertEqual(solution.QuestionsMarks('9???1???9??1???9'), 'false')

    def test_FindIntersection(self):
        self.assertEqual(solution.FindIntersection(
            ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]), '1,4,13')
        self.assertEqual(solution.FindIntersection(
            ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]), '1,9,10')
        self.assertEqual(solution.FindIntersection(["2, 3, 4", "3"]), '3')

    def test_EquivalentKeypresses(self):
        self.assertEqual(solution.EquivalentKeypresses(
            ["a,b,c,d", "a,b,c,d,-B,d"]), 'true')
        self.assertEqual(solution.EquivalentKeypresses(
            ["c,a,r,d", "c,a,-B,r,d"]), 'false')
        self.assertEqual(solution.EquivalentKeypresses(
            ["q,w,e,r,t,y", "-B,-B,q,w,w,-B,e,r,t,y"]), 'true')
        self.assertEqual(solution.EquivalentKeypresses(
            ["", "-B,-B,-B"]), 'true')
        self.assertEqual(solution.EquivalentKeypresses(
            ["s,t,r,e,e,t", "-B,s,s,-B,t,r,e,e,t"]), 'true')

    def test_KaprekarsConstant(self):
        self.assertEqual(solution.KaprekarsConstant(2111), 5)
        self.assertEqual(solution.KaprekarsConstant(9831), 7)
        self.assertEqual(solution.KaprekarsConstant(3524), 3)

    def test_ChessboardTraveling(self):
        self.assertEqual(solution.ChessboardTraveling("(1 1)(3 3)"), 6)
        self.assertEqual(solution.ChessboardTraveling("(2 2)(4 3)"), 3)

    def test_MaximalSquare(self):
        self.assertEqual(solution.MaximalSquare(
            ["0111", "1111", "1111", "1111"]), 9)
        self.assertEqual(solution.MaximalSquare(["0111", "1101", "0111"]), 1)


if __name__ == '__main__':
    unittest.main()
