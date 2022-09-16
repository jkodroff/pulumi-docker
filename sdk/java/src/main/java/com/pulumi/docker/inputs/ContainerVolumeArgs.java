// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.docker.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ContainerVolumeArgs extends com.pulumi.resources.ResourceArgs {

    public static final ContainerVolumeArgs Empty = new ContainerVolumeArgs();

    /**
     * The path in the container where the volume will be mounted.
     * 
     */
    @Import(name="containerPath")
    private @Nullable Output<String> containerPath;

    /**
     * @return The path in the container where the volume will be mounted.
     * 
     */
    public Optional<Output<String>> containerPath() {
        return Optional.ofNullable(this.containerPath);
    }

    /**
     * The container where the volume is coming from.
     * 
     */
    @Import(name="fromContainer")
    private @Nullable Output<String> fromContainer;

    /**
     * @return The container where the volume is coming from.
     * 
     */
    public Optional<Output<String>> fromContainer() {
        return Optional.ofNullable(this.fromContainer);
    }

    /**
     * The path on the host where the volume is coming from.
     * 
     */
    @Import(name="hostPath")
    private @Nullable Output<String> hostPath;

    /**
     * @return The path on the host where the volume is coming from.
     * 
     */
    public Optional<Output<String>> hostPath() {
        return Optional.ofNullable(this.hostPath);
    }

    /**
     * If `true`, this volume will be readonly. Defaults to `false`.
     * 
     */
    @Import(name="readOnly")
    private @Nullable Output<Boolean> readOnly;

    /**
     * @return If `true`, this volume will be readonly. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> readOnly() {
        return Optional.ofNullable(this.readOnly);
    }

    /**
     * The name of the docker volume which should be mounted.
     * 
     */
    @Import(name="volumeName")
    private @Nullable Output<String> volumeName;

    /**
     * @return The name of the docker volume which should be mounted.
     * 
     */
    public Optional<Output<String>> volumeName() {
        return Optional.ofNullable(this.volumeName);
    }

    private ContainerVolumeArgs() {}

    private ContainerVolumeArgs(ContainerVolumeArgs $) {
        this.containerPath = $.containerPath;
        this.fromContainer = $.fromContainer;
        this.hostPath = $.hostPath;
        this.readOnly = $.readOnly;
        this.volumeName = $.volumeName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ContainerVolumeArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ContainerVolumeArgs $;

        public Builder() {
            $ = new ContainerVolumeArgs();
        }

        public Builder(ContainerVolumeArgs defaults) {
            $ = new ContainerVolumeArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param containerPath The path in the container where the volume will be mounted.
         * 
         * @return builder
         * 
         */
        public Builder containerPath(@Nullable Output<String> containerPath) {
            $.containerPath = containerPath;
            return this;
        }

        /**
         * @param containerPath The path in the container where the volume will be mounted.
         * 
         * @return builder
         * 
         */
        public Builder containerPath(String containerPath) {
            return containerPath(Output.of(containerPath));
        }

        /**
         * @param fromContainer The container where the volume is coming from.
         * 
         * @return builder
         * 
         */
        public Builder fromContainer(@Nullable Output<String> fromContainer) {
            $.fromContainer = fromContainer;
            return this;
        }

        /**
         * @param fromContainer The container where the volume is coming from.
         * 
         * @return builder
         * 
         */
        public Builder fromContainer(String fromContainer) {
            return fromContainer(Output.of(fromContainer));
        }

        /**
         * @param hostPath The path on the host where the volume is coming from.
         * 
         * @return builder
         * 
         */
        public Builder hostPath(@Nullable Output<String> hostPath) {
            $.hostPath = hostPath;
            return this;
        }

        /**
         * @param hostPath The path on the host where the volume is coming from.
         * 
         * @return builder
         * 
         */
        public Builder hostPath(String hostPath) {
            return hostPath(Output.of(hostPath));
        }

        /**
         * @param readOnly If `true`, this volume will be readonly. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder readOnly(@Nullable Output<Boolean> readOnly) {
            $.readOnly = readOnly;
            return this;
        }

        /**
         * @param readOnly If `true`, this volume will be readonly. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder readOnly(Boolean readOnly) {
            return readOnly(Output.of(readOnly));
        }

        /**
         * @param volumeName The name of the docker volume which should be mounted.
         * 
         * @return builder
         * 
         */
        public Builder volumeName(@Nullable Output<String> volumeName) {
            $.volumeName = volumeName;
            return this;
        }

        /**
         * @param volumeName The name of the docker volume which should be mounted.
         * 
         * @return builder
         * 
         */
        public Builder volumeName(String volumeName) {
            return volumeName(Output.of(volumeName));
        }

        public ContainerVolumeArgs build() {
            return $;
        }
    }

}