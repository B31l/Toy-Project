using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class HomeDirector : MonoBehaviour {

    public void BtnAct0Down() {
        SceneManager.LoadScene("Act0Scene");
    }
    public void BtnAct1Down() {
        SceneManager.LoadScene("Act1Scene");
    }
    public void BtnAct2Down() {
        SceneManager.LoadScene("Act2Scene");
    }
    public void BtnAct3Down() {
        SceneManager.LoadScene("Act3Scene");
    }
    public void BtnHomeDown() {
        SceneManager.LoadScene("HomeScene");
    }
}
