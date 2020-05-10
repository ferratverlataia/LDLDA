import pyclipper
def sutherland (subj,clip):
   subj = (
      ((180, 200), (260, 200), (260, 150), (180, 150)),
      ((0, 0), (0, 0), (0, 0))
   )
   print(type(subj))
   clip = ((190, 210), (240, 210), (240, 130), (190, 130))

   pc = pyclipper.Pyclipper()
   pc.AddPath(clip, pyclipper.PT_CLIP, True)
   pc.AddPaths(subj, pyclipper.PT_SUBJECT, True)

   solution = pc.Execute(pyclipper.CT_INTERSECTION, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD)
   print(solution)
   return solution

sutherland()