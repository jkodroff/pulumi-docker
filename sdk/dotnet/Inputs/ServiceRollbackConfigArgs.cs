// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class ServiceRollbackConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Delay between restart attempts `(ms|s|m|h)`
        /// all tasks are up when a service is created, or to check if all tasks are successfully updated on an update. Default: `7s`.
        /// </summary>
        [Input("delay")]
        public Input<string>? Delay { get; set; }

        /// <summary>
        /// Action on update failure: `pause|continue|rollback`.
        /// </summary>
        [Input("failureAction")]
        public Input<string>? FailureAction { get; set; }

        /// <summary>
        /// The failure rate to tolerate during an update as `float`. **Important:** the `float`need to be wrapped in a `string` to avoid internal
        /// casting and precision errors.
        /// </summary>
        [Input("maxFailureRatio")]
        public Input<string>? MaxFailureRatio { get; set; }

        /// <summary>
        /// Duration after each task update to monitor for failure `(ns|us|ms|s|m|h)`
        /// </summary>
        [Input("monitor")]
        public Input<string>? Monitor { get; set; }

        /// <summary>
        /// Update order either 'stop-first' or 'start-first'.
        /// </summary>
        [Input("order")]
        public Input<string>? Order { get; set; }

        /// <summary>
        /// The maximum number of tasks to be updated in one iteration simultaneously (0 to update all at once).
        /// </summary>
        [Input("parallelism")]
        public Input<int>? Parallelism { get; set; }

        public ServiceRollbackConfigArgs()
        {
        }
    }
}
