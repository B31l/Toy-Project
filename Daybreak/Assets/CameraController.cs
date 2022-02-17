using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour {

    GameObject player;
    const float MAX_RIGHT = 14.0f;
    const float MAX_LEFT = -14.0f;

    void Start() {
        this.player = GameObject.Find("player");
    }

    void Update() {

        Vector3 playerPos = this.player.transform.position;
        float temp;

        if (playerPos.x < MAX_LEFT) temp = MAX_LEFT;
        else if (playerPos.x > MAX_RIGHT) temp = MAX_RIGHT;
        else temp = playerPos.x;

        transform.position = new Vector3(temp, playerPos.y + 1.0f, transform.position.z);
    }
}
