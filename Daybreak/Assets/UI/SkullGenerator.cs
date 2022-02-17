using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SkullGenerator : MonoBehaviour {

    public GameObject HomeSkullPrefab;
    float span = 0.1f;
    float delta = 0;

    void Update() {
        this.delta += Time.deltaTime;
        if(this.delta > this.span) {
            this.delta = 0;
            GameObject go = Instantiate(HomeSkullPrefab) as GameObject;
            float px = Random.Range(-4.0f, 4.0f);
            go.transform.position = new Vector3(px, 7, 0);
        }
    }
}
