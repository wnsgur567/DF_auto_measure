import image_sampling as sp
from gui_app import MyApp
from cv2 import cv2


class Measure:
    def __init__(self):
        self.origin_image_hist = [
            sp.get_histogram(cv2.imread('frame_img/0.png')),
            sp.get_histogram(cv2.imread('frame_img/1.png')),
            sp.get_histogram(cv2.imread('frame_img/2.png')),
            sp.get_histogram(cv2.imread('frame_img/3.png')),
            sp.get_histogram(cv2.imread('frame_img/4.png')),
            sp.get_histogram(cv2.imread('frame_img/5.png')),
        ]

    # 모두 0.95 보다 크면
    def compare_img(self, img_histogram) -> bool:
        sum = 0
        for origin_hist in self.origin_image_hist:
            sum += cv2.compareHist(origin_hist, img_histogram, cv2.HISTCMP_CORREL)
        avg = sum / len(self.origin_image_hist)
        if avg > 0.95:
            return True
        else:
            return False

    def main_loop_action(self):
        print('loop...')
        x, y, w, h = MyApp.instance.get_rect()
        img = sp.capture_img(x, y, w, h)
        hist = sp.get_histogram(img)

        # 파티 신청 프레임이라고 판단되면..
        if self.compare_img(hist):
            print('통과!')
        else:
            print('없어!')

    def run(self):
        MyApp.run(self.main_loop_action)


if __name__ == '__main__':
    m = Measure()
    m.run()
