import cv2

def reverse_video(video_path, output_path="reversed_video.mp4"):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    
    frames = []
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0 or fps != fps:
        fps = 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        if len(frames) >= 150:
            break
            
    cap.release()
    
    if len(frames) == 0:
        print("No frames captured!")
        return

    frames.reverse()
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for f in frames:
        out.write(f)
        cv2.imshow("Reversed Video", f)
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break
            
    out.release()
    cv2.destroyAllWindows()

reverse_video("video.mp4")
