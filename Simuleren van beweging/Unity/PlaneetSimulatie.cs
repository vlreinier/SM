using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlaneetSimulatie : MonoBehaviour
{
    public Vector3 Acceleration;
    public Vector3 Velocity;
	public GameObject center;
	public float gravity;
    public Camera camera;

    // Start is called before the first frame update
    void Start()
    {
        gravity = 10;
        Rigidbody this_RB = gameObject.GetComponent<Rigidbody>();
        Rigidbody center_RB = center.gameObject.GetComponent<Rigidbody>();

        // camera setup
        camera.enabled = true;
    }

    Vector3 Orbit_Acceleration(Vector3 difference)
    {
        return difference * gravity / (float)Math.Pow(difference.magnitude, 3);
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        Acceleration = Orbit_Acceleration(-transform.position - center.transform.position);
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;
    }

    void LateUpdate()
    {
        camera.transform.LookAt(transform.position);
    }
}
