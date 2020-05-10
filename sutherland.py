import pyclipper
def sutherland (su, clip):
   subj = []
   su = set(su)
   su = tuple(su)
   print(su)
   subj.append(su)
   subj.append(((0, 0), (0, 0), (0, 0)))
   subj = tuple(subj)
   clip = set(clip)
   clip = tuple(clip)
   pc = pyclipper.Pyclipper()
   pc.AddPath(clip, pyclipper.PT_CLIP, True)
   pc.AddPaths(subj, pyclipper.PT_SUBJECT, True)

   solution = pc.Execute(pyclipper.CT_INTERSECTION, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD)
   print(solution)
   return solution
