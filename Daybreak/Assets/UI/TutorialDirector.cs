using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class TutorialDirector : MonoBehaviour {

    int page = 0;
    int pageMaxIndex = 3;
    GameObject Message;
    GameObject BtnPrevious, BtnNext;
    GameObject Des_player, Des_goal, Des_tree, Des_skull;
    string[] message = {
        "좌우 방향키와 스페이스 바로 조작합니다",
        "아침이 되기 전에 집으로 숨어야 합니다",
        "푸른 해골로 시간을 늦출 수 있습니다",
        "나무 위에 올라갈 수 있습니다"
    };

    void Start() {
        this.Message = GameObject.Find("Message");
        this.BtnPrevious = GameObject.Find("BtnPrevious");
        this.BtnNext = GameObject.Find("BtnNext");

        this.Des_player = GameObject.Find("Des_player");
        this.Des_goal = GameObject.Find("Des_goal");
        this.Des_skull = GameObject.Find("Des_skull");
        this.Des_tree = GameObject.Find("Des_tree");
    }

    void Update() {

        /* 메세지 */
        if (page == 0) {
            this.BtnPrevious.SetActive(false);
        } else if (page == pageMaxIndex) {
            this.BtnNext.SetActive(false);
        } else {
            this.BtnPrevious.SetActive(true);
            this.BtnNext.SetActive(true);
        }
        this.Message.GetComponent<Text>().text = message[page];


        /* 그림 */
        this.Des_player.SetActive(false);
        this.Des_goal.SetActive(false);
        this.Des_skull.SetActive(false);
        this.Des_tree.SetActive(false);

        switch (page) {
            case 0:
                this.Des_player.SetActive(true);
                break;
            case 1:
                this.Des_goal.SetActive(true);
                break;
            case 2:
                this.Des_skull.SetActive(true);
                break;
            case 3:
                this.Des_tree.SetActive(true);
                break;
        }
    }

    public void BtnPreviousDown() {
        page--;
    }

    public void BtnNextDown() {
        page++;
    }
}
