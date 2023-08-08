import mediapipe as mp
import cv2
import csv

# Khai báo đối tượng cho MediaPipe Hands và MediaPipe Face Mesh
mp_hands = mp.solutions.hands.Hands()
mp_face_mesh = mp.solutions.face_mesh.FaceMesh()

# Khai báo đối tượng cho việc đọc dữ liệu từ webcam (hoặc video)
cap = cv2.VideoCapture(0)  # Thay 0 bằng đường dẫn file video nếu bạn muốn sử dụng video thay vì webcam

csv_file = open('hi.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
i = 0
while cap.isOpened():
    i += 1
    success, image = cap.read()
    if not success:
        break

    # Chuyển đổi hình ảnh từ BGR sang RGB vì MediaPipe sử dụng định dạng RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Sử dụng MediaPipe Hands để nhận diện bàn tay
    results_hands = mp_hands.process(image_rgb)

    # Vẽ các điểm mốc trên tay và đoạn thẳng nối chúng
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            for id, landmark in enumerate(hand_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1)

                if id == 0:
                    start_x, start_y = cx, cy
                else:
                    end_x, end_y = cx, cy
                    cv2.line(image, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)
                    start_x, start_y = end_x, end_y
            hand_data = [landmark.x for landmark in hand_landmarks.landmark]  # Lưu tọa độ x của các điểm mốc
            csv_writer.writerow(hand_data)
    # Sử dụng MediaPipe Face Mesh để nhận diện khuôn mặt
    results_face_mesh = mp_face_mesh.process(image_rgb)

    # Vẽ các điểm mốc trên khuôn mặt và đoạn thẳng nối chúng
    if results_face_mesh.multi_face_landmarks:
        for face_landmarks in results_face_mesh.multi_face_landmarks:
            for landmark in face_landmarks.landmark:
                h, w, c = image.shape
                x, y = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
            face_data = [landmark.x for landmark in face_landmarks.landmark]  # Lưu tọa độ x của các điểm mốc
            csv_writer.writerow(face_data)
    # Hiển thị kết quả lên màn hình
    cv2.imshow('Hand and Face Landmarks', image)
    print(i)
    if i > 600:
        break
    # Nhấn 'q' để thoát
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Giải phóng bộ nhớ và đóng cửa sổ video
csv_file.close()
cap.release()
cv2.destroyAllWindows()
