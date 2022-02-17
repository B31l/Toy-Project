using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameDirector : MonoBehaviour {

    GameObject TimeGuageNeddle;
    GameObject Information, ClearMessage, DeadMessage;
    GameObject BtnHome, BtnRestart;

    GameObject player, goal, skull;
    GameObject bg_night, bg_daybreak, bg_morning;

    float timePresent = 0;          // 시작 지점
    float timeMid = 1080.0f;        // 중간 지점
    float timeMax = 1440.0f;        // 종료 지점
    float timeSpeed = 0.3f;         // 시간의 흐름 속도
    float timeSkull = 720.0f;       // 해골로 얻는 시간

    void Start() {

        this.TimeGuageNeddle = GameObject.Find("TimeGuageNeddle");
        this.Information = GameObject.Find("Information");
        this.ClearMessage = GameObject.Find("ClearMessage");
        this.DeadMessage = GameObject.Find("DeadMessage");
        this.BtnHome = GameObject.Find("BtnHome");
        this.BtnRestart = GameObject.Find("BtnRestart");

        this.player = GameObject.Find("player");
        this.goal = GameObject.Find("goal");
        this.skull = GameObject.Find("skull");
        this.bg_night = GameObject.Find("bg_night");
        this.bg_daybreak = GameObject.Find("bg_daybreak");
        this.bg_morning = GameObject.Find("bg_morning");

        bg_night.SetActive(false);
        bg_daybreak.SetActive(false);
        bg_morning.SetActive(false);
        Information.SetActive(false);
        BtnHome.SetActive(false);
        BtnRestart.SetActive(false);
    }

    void Update() {
            
        /* 게이지 이동 */
        this.TimeGuageNeddle.transform.Translate(timeSpeed, 0, 0);

        /* 배경 변경 : SetActive 사용 */
        timePresent += timeSpeed;                       
        if (timePresent < timeMid) {
            bg_night.SetActive(true);
        } 
        else if (timePresent < timeMax) {
            bg_daybreak.SetActive(true);
        } 
        else {
            bg_morning.SetActive(true);
            timeSpeed = 0;
            this.player.GetComponent<PlayerController>().Dead();

            this.DeadMessage.GetComponent<Text>().text = "DEAD";
            Information.SetActive(true);
            BtnHome.SetActive(true);
            BtnRestart.SetActive(true);
        }

        /* player와 goal 충돌 */
        Vector2 p1 = this.player.transform.position;
        Vector2 p2 = this.goal.transform.position;
        Vector2 dirGoal = p1 - p2;
        float dg = dirGoal.magnitude;
        float rg = 2.5f;
        if (dg < rg) {
            /* 게임 정지 */
            timeSpeed = 0;
            /* UI */
            this.ClearMessage.GetComponent<Text>().text = "CLEAR";
            Information.SetActive(true);
            BtnHome.SetActive(true);
            BtnRestart.SetActive(true);
        }

        /* player와 skull 충돌 */
        Vector2 p3 = this.skull.transform.position;
        Vector2 dirSkull = p1 - p3;
        float ds = dirSkull.magnitude;
        float rs = 1.5f;
        if (ds < rs) {
            /* 감소량만큼 시간 감소 */
            if (timePresent >= timeSkull) {
                this.TimeGuageNeddle.transform.Translate(-timeSkull, 0, 0);
                timePresent -= timeSkull;
            }
            /* 현재 시간이 감소량보다 적으면 0으로 초기화  */
            else {
                this.TimeGuageNeddle.transform.Translate(-timePresent, 0, 0);
                timePresent = 0;
            }
            this.skull.SetActive(false);
        }
    }
}
