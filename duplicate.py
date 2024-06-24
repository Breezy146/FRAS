import pandas as pd
import csv

# df_state=pd.read_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Teampmc.csv")

# Dup_Rows = df_state[df_state.duplicated()]

# print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))

# DF_RM_DUP = df_state.drop_duplicates(keep=False)

# print('\n\nResult DataFrame after duplicate removal :\n', DF_RM_DUP.head(n=1))


# df_state=pd.read_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Teampmc23.csv")
df_state = pd.read_csv(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Teampmc23.csv")

    
        # Dup_Rows = df_state[df_state.duplicated()]

DF_RM_DUP = df_state.drop_duplicates(keep=False)
# data = DF_RM_DUP.head(n=1)


# DF_RM_DUP = df_state.drop_duplicates(subset=['C'], keep='last')  


        # print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))

        # DF_RM_DUP = df_state.drop_duplicates(keep=False)
    # writer=csv.writer(DF_RM_DUP.head(n=1))

# (data = DF_RM_DUP.head(n=1)
# # data.to_csv('teampmc1.csv')
# with open("test.csv", "wt") as fp:
#     writer = csv.writer(fp)
#     # writer.writerow(["your", "header", "foo"])  # write header
#     writer.writerow(data)
# )

DF_RM_DUP.to_csv('test1.csv', index=False) 

# print('\n\nResult DataFrame after duplicate removal :\n', DF_RM_DUP.head(n=1))
# data = DF_RM_DUP.head(n=1)

# with open('teampmc1.csv', 'w', encoding='UTF8') as data:
#     writer = csv.writer(data)
#     writer.writerow(data)

#     data.close()






